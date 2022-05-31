from django import views
import requests
import re
from bs4 import BeautifulSoup
from googletrans import Translator
from . models import Novel, Chapter, Schedule
from slugify import slugify
import datetime
import pytz

translator = Translator()
def translate(text):
    return translator.translate(text, dest = 'en').text
def distancefromthousand(elem):
    return elem%1000
def download(URL,genres,tags):
    try:
       Novel.objects.get(url=URL).delete()
    except Novel.DoesNotExist:
        pass
    response = requests.get(URL,headers={"User-Agent":"Mozilla/5.0"}).text
    novel_obj = BeautifulSoup(response, "html.parser")
    chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
    jp_title = novel_obj.title.text
    en_title = translate(jp_title)
    novel_id = slugify(en_title)
    release = int(novel_obj.find(class_='long_update').text.strip()[:4])
    new_novel = Novel.objects.create(
        id = novel_id,
        title = en_title,
        alternativetitle = jp_title,
        url = URL,
        author = translate(novel_obj.find(class_ = "novel_writername").text)[8:],
        description = translate(novel_obj.find(id = 'novel_ex').text.replace('<br />','&#013;&#010;')),
        genres = ",".join(genres),
        tags = ",".join(tags),
        status = 0,
        release = release,
        completed = 0,
        active=0,
        views=0
    )
    processChapeters(chapternumber=1,section=0,new_novel=new_novel,chapter_list=chapter_list)
def update(novel):
    for novel in Novel.objects.filter(completed=0):
        response = requests.get(novel.url,headers={"User-Agent":"Mozilla/5.0"}).text
        novel_obj = BeautifulSoup(response, "html.parser")
        chapters = Chapter.objects.filter(novel=novel).order_by('chapterNumber')
        chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
        if len(chapter_list) > len(chapters):
            chapter_list = chapter_list[len(chapters):]
            last_chapter = chapters.last()
            chapternumber = last_chapter.chapterNumber+1
            section = last_chapter.section
            processChapeters(chapternumber=chapternumber,section=section,new_novel=novel,chapter_list=chapter_list)
        r = requests.get(novel.url[:25]+'/novelview/infotop/ncode'+novel.url[25:],headers={"User-Agent":"Mozilla/5.0"}).text
        o=BeautifulSoup(r,'html.parser')
        if o.find(id='noveltype'):
            novel.completed = 1
        novel.save()
        
        


def processChapeters(chapternumber,section,new_novel,chapter_list):
    removals = {"<ruby>":'',"</ruby>":'',"<rb>":'',"</rb>":'',"<rp>":'',"</rp>":'',"<br>":'&#013;&#010;','<br/>':'','</p>':'&#013;&#010;'}
    novel_id = new_novel.id
    for i in range(len(chapter_list)):
        ch_id = slugify(novel_id+"s"+str(section)+"c"+str(chapternumber))
        print(type(ch_id))
        if 'class' in str(chapter_list[i]):
            section+=1
            Chapter.objects.create(id=ch_id,novel=new_novel,title=translate(chapter_list[i].text),section=section,chapterNumber=0, chapterOrder=chapternumber+section, active=5)
        else:
            content = ""
            chapter_obj = BeautifulSoup(requests.get("https://ncode.syosetu.com" + str(chapter_list[i]['href']),headers={"User-Agent":"Mozilla/5.0"}).text, "html.parser")
            text = '   '+'   '.join([str(p)[str(p).index(">")+1:] for p in chapter_obj.find(id = 'novel_honbun').find_all("p")])
            #process text content
            for key,value in removals.items():text = text.replace(key,value)
            while "</rt>" in text:text = text[:text.index("<rt>")-1] + text[text.index("</rt>")+6:]
            newlines=[_.start() for _ in re.finditer('&#013;&#010;', text)]
            newlines.sort(key=distancefromthousand)
            divide_index={0:0}
            for line in newlines:
                if line//1000 !=0 and line//1000 not in divide_index:
                    divide_index[line//1000]=line
            divide_index[len(divide_index)]=len(text)
            divide_index=dict(sorted(divide_index.items(), key=lambda item: item[1]))
            for i in range(len(divide_index)-1):content += translate(text[divide_index[i]:divide_index[i+1]])
            chapter_title = translate(str(chapter_obj.find(class_ = 'novel_subtitle').text))
            Chapter.objects.create(
                id=ch_id,
                novel = new_novel,
                title = chapter_title,
                content = content,
                chapterNumber=chapternumber,
                section=section,
                active=5,
                chapterOrder=chapternumber+section)
            chapternumber += 1
def upload():
    now = pytz.timezone('America/Los_Angeles') 
    now = datetime.datetime.now(now)
    try:
        schedule = Schedule.objects.get(day=now.strftime("%A"),time=now.strftime("%H"))
        novel = schedule.novel
        chapters = Chapter.objects.filter(novel=novel)
        for i in range(4,-1,-1):
            latest_chapters = chapters.filter(active=i).last().chapterOrder
            try:
                new_chapter = Chapter.object.get(chapterOrder=latest_chapters+1)
            except Chapter.DoesNotExist:
                continue
            new_chapter.active = i
            new_chapter.date = now
            if not new_chapter.content:
                i+=1
            new_chapter.save()
    except:
        print('no uploads now')


        

    