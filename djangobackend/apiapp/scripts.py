from django import views
import requests
import re
from bs4 import BeautifulSoup
from googletrans import Translator
from . models import Novel, Chapter, Schedule
from slugify import slugify
import datetime
import pytz
import language_tool_python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

translator = Translator()
tool = language_tool_python.LanguageTool('en-US')
def translate(text):
    return translator.translate(text, dest = 'en').text
def distance_from_thousand(elem):
    return elem%1000
def correct_grammer(text):
    my_mistakes = []
    my_corrections = []
    start_positions = []
    end_positions = []
    matches = [a for a in tool.check(text) if a.category != 'TYPOS' and '   ' not in  a.context]
    for rules in matches:
        if len(rules.replacements)>0:
            start_positions.append(rules.offset)
            end_positions.append(rules.errorLength+rules.offset)
            my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
            my_corrections.append(rules.replacements[0]) 
    my_new_text = list(text)
    for m in range(len(start_positions)):
        for i in range(len(text)):
            my_new_text[start_positions[m]] = my_corrections[m]
            if (i>start_positions[m] and i<end_positions[m]):
                my_new_text[i]=""
     
    my_new_text = "".join(my_new_text)
    return my_new_text

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
        description = correct_grammer(translate(novel_obj.find(id = 'novel_ex').text.replace('<br />','&#013;&#010;   '))),
        genres = ",".join(genres),
        tags = ",".join(tags),
        status = 0,
        release = release,
        completed = 0,
        active=0,
        views=0
    )
    processChapeters(chapter_number=1,section=0,new_novel=new_novel,chapter_list=chapter_list)
def update(novel):
    for novel in Novel.objects.filter(completed=0):
        response = requests.get(novel.url,headers={"User-Agent":"Mozilla/5.0"}).text
        novel_obj = BeautifulSoup(response, "html.parser")
        chapters = Chapter.objects.filter(novel=novel).order_by('chapterNumber')
        chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
        if len(chapter_list) > len(chapters):
            chapter_list = chapter_list[len(chapters):]
            last_chapter = chapters.last()
            chapter_number = last_chapter.chapterNumber+1
            section = last_chapter.section
            processChapeters(chapter_number=chapter_number,section=section,new_novel=novel,chapter_list=chapter_list)
        r = requests.get(novel.url[:25]+'/novelview/infotop/ncode'+novel.url[25:],headers={"User-Agent":"Mozilla/5.0"}).text
        o=BeautifulSoup(r,'html.parser')
        if o.find(id='noveltype'):
            novel.completed = 1
        novel.save()
        
def processChapeters(chapter_number,section,new_novel,chapter_list):
    removals = {"<ruby>":'',"</ruby>":'',"<rb>":'',"</rb>":'',"<rp>":'',"</rp>":'',"<br>":'&#013;&#010;','<br/>':'','</p>':'&#013;&#010;'}
    novel_id = new_novel.id
    for i in range(len(chapter_list)):
        ch_id = slugify(novel_id+"s"+str(section)+"c"+str(chapter_number))
        print(type(ch_id))
        if 'class' in str(chapter_list[i]):
            section+=1
            Chapter.objects.create(id=ch_id,novel=new_novel,title=translate(chapter_list[i].text),section=section,chapterNumber=0, chapterOrder=chapter_number+section, active=5)
        else:
            content = ""
            chapter_obj = BeautifulSoup(requests.get("https://ncode.syosetu.com" + str(chapter_list[i]['href']),headers={"User-Agent":"Mozilla/5.0"}).text, "html.parser")
            text = '   '+'   '.join([str(p)[str(p).index(">")+1:] for p in chapter_obj.find(id = 'novel_honbun').find_all("p")])
            #process text content
            for key,value in removals.items():text = text.replace(key,value)
            while "</rt>" in text:text = text[:text.index("<rt>")-1] + text[text.index("</rt>")+6:]
            new_lines=[_.start() for _ in re.finditer('&#013;&#010;', text)]
            new_lines.sort(key=distance_from_thousand)
            divide_index={0:0}
            
            for line in new_lines:
                if line//1000 !=0 and line//1000 not in divide_index:
                    divide_index[line//1000]=line
            divide_index[len(divide_index)]=len(text)
            divide_index=dict(sorted(divide_index.items(), key=lambda item: item[1]))
            for i in range(len(divide_index)-1):content += translate(text[divide_index[i]:divide_index[i+1]])
            if(chapter_number==1):
                print(tool.check(content))
            content = correct_grammer(content)
            chapter_title = translate(str(chapter_obj.find(class_ = 'novel_subtitle').text))
            Chapter.objects.create(
                id=ch_id,
                novel = new_novel,
                title = chapter_title,
                content = content,
                chapterNumber=chapter_number,
                section=section,
                active=5,
                chapterOrder=chapter_number+section)
            chapter_number += 1
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
            if new_chapter.content=='' or not new_chapter.content:
                i+=1
            new_chapter.save()
            botupload(new_chapter,now)
    except:
        print('no uploads now')
    

def botupload(chapter,today):
    chapter.active = True
    chapter.date = today.strftime("%B %d, %Y")
    novel= Novel.objects.get(title=chapter.novel)
    novel.last_updated = today.strftime("%B %d, %Y")
    link = "http://localhost:8080/novel/"+novel.novel_id+"/"+str(chapter.chapternumber)
    novel_title = novel.title
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://www.novelupdates.com')
    browser.find_element(by=By.LINK_TEXT, value='Login').click()
    browser.find_element(by=By.NAME, value='log').send_keys("jgooso")
    browser.find_element(by=By.NAME, value='pwd').send_keys("testingpassword")
    browser.find_element(by=By.NAME, value='wp-submit').click()
    browser.find_elements(by=By.ID, value='menu_right_item')[1].click()
    browser.find_element(by=By.LINK_TEXT, value='User Profile').click()
    browser.find_element(by=By.PARTIAL_LINK_TEXT, value='Release').click()
    browser.find_element(by=By.ID, value='title_change_100').send_keys(novel_title)
    browser.find_element(by=By.NAME, value='arrelease').send_keys(chapter)
    browser.find_element(by=By.NAME, value='arlink').send_keys(link)
    browser.find_element(by=By.ID, value='group_change_100').send_keys("tententranslations")
    novel.save()



        

    