from typing import Type
import mysql.connector

#downloading novels and chapters
import re
import requests
from slugify import slugify
import language_tool_python
from bs4 import BeautifulSoup
from googletrans import Translator
from deep_translator import GoogleTranslator
import json

#uploading chapters to weboage
import datetime
import pytz
from selenium import webdriver

#Basic intialializations

'''
config = {
'user': 'jgooso',
'password': '<{;}eX2"ZcqGTBtl',
'host': '35.236.68.50',
'port': '3306',
'database': 'novels',
'raise_on_warnings': True,}
'''
config = {
'user': 'root',
'password': 'jeg4Iphone',
'host': '127.0.0.1',
'port': '3306',
'database': 'tententranslations',
'raise_on_warnings': True,}
noveldb = mysql.connector.connect(**config)
novelcursor = noveldb.cursor(buffered=True)
translator = Translator()
tool = language_tool_python.LanguageTool('en-US')

#Commonly used Functions
def translate(text):#Translate text
    return translator.translate(text).text
def deeptranslate(text):
    return GoogleTranslator(source='auto', target='en').translate(text)
def get_HTML(URL):#retrieve HTML from webpage
    response = requests.get(URL,headers={"User-Agent":"Mozilla/5.0"}).text
    return BeautifulSoup(response, "html.parser")

def distance_from_thousand(elem):#sort function for translations
    return elem%1000

def correct_grammer(text):#corrects grammers. Ignores spelling mistakes
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
def scrub_HTML(text):
    html_special_characters={
         '&':'&#38;',
        '<':'&#60;',
        '>':'&#62;',
        '"':'&#34;',
        "'":'&#39;',
        '¥':'&#165;',
        '(・)':''
    }
    for key,value in html_special_characters.items():text = text.replace(key,value)
    return text
def remove_html_tags(text):
    text = text.replace('</p>','\n')
    clean = re.compile('<.*?>')
    return re.sub(clean,'',text)



def download(URL,genres,tags):#download novels from NCODE.SYOSETU
    #Retrieve elements from webpage
    novel_obj = get_HTML(URL)
    jp_title = novel_obj.title.text
    en_title = translate(jp_title)
    novel_id = slugify(en_title)
    release = int(novel_obj.find(class_='long_update').text.strip()[:4])

    #DElETE novel from database if it already exists
    delete_sql = "DELETE FROM novels WHERE novelid = %s"
    delete_val = (novel_id,)
    novelcursor.execute(delete_sql,delete_val)

    #INSERT data into database
    novel_insert_sql = "INSERT INTO novels VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    novel_insert_val = (
        novel_id,#novelid
        en_title,#title
        jp_title,#alternativetitle
        URL,#url
        scrub_HTML(translate(novel_obj.find(class_ = "novel_writername").text)[8:]),#author
        genres,#genres
        tags,#tags
        release,#novelrelease
        'Ongoing',#uploadstatus
        'Ongoing',#completed
        0,#views
        0,#ratings
        scrub_HTML(correct_grammer(translate(novel_obj.find(id = 'novel_ex').text.replace('<br />','&#013;&#010;   ')))),#description
        0,#novelactive
        None,#lastupload
        None,#firstupload
        None#imageurl
    )
    novelcursor.execute(novel_insert_sql,novel_insert_val)
    descriptors = genres = genres.split(',') + tags.split(',')
    for d in descriptors:
        print(d)
        descriptor_insert_sql = 'INSERT INTO noveldescriptors (novelid,descriptor) VALUES (%s,%s)'
        descriptor_insert_val = (novel_id,d.strip())
        novelcursor.execute(descriptor_insert_sql,descriptor_insert_val)
    #Upload Chapters
    chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
    processChapters(chapter_number=1,section=0,chapter_list=chapter_list,novel_id=novel_id)
    noveldb.commit()

def processChapters(chapter_number,section,novel_id,chapter_list):#Translates chapters and processes them to be easier to read
    sql = "INSERT INTO chapters (chapterid,novelid,title,section,chapternumber,content,chapteractive,chapterorder) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    for i in range(len(chapter_list)-1):
        print(chapter_number)
        ch_id = slugify(novel_id+"s"+str(section)+"c"+str(chapter_number))
        if 'class' in str(chapter_list[i]):
            section+=1
            val = (
                ch_id,#id
                novel_id,#novelid
                translate(chapter_list[i].text),#title
                section,#section
                 0,#chapternumber
                None,#content
                5,#active
                chapter_number+section,#chapterorder
            )
            novelcursor.execute(sql,val)
        else:
            chapter_obj = get_HTML("https://ncode.syosetu.com" + str(chapter_list[i]['href']))
            chapter_title = translate(str(chapter_obj.find(class_ = 'novel_subtitle').text))
            content = ""
            text = '   '+'   '.join([str(p)[str(p).index(">")+1:] for p in chapter_obj.find(id = 'novel_honbun').find_all("p")])
            #process text content
            text = remove_html_tags(text)
            while "</rt>" in text:text = text[:text.index("<rt>")-1] + text[text.index("</rt>")+6:]

            #find good points of division
            new_lines=[_.start() for _ in re.finditer('<br>', text)]
            new_lines.sort(key=distance_from_thousand)
            divide_index={0:0}
            for line in new_lines:
                if line//200 !=0 and line//200 not in divide_index:
                    divide_index[line//200]=line
            divide_index[len(divide_index)]=len(text)
            divide_index=dict(sorted(divide_index.items(), key=lambda item: item[1]))

            #translate and grammer check chapters
            for j in range(len(divide_index)-1):content += translate(text[divide_index[j]:divide_index[j+1]])
            content = correct_grammer(content)
            content = scrub_HTML(content)
            val = (
                ch_id,#id
                novel_id,#novelid
                chapter_title,#chaptertitle
                section,#section
                chapter_number,#chapternumber
                content,#content
                5,#chapteractive
                chapter_number+section,#chapterorder
            )
            novelcursor.execute(sql,val)
            chapter_number += 1

def update():#Search for new chapters and download them to database
    novelcursor.execute("SELECT novelid,url FROM novels WHERE completed = 'Ongoing' OR completed = 'On Hold'")
    novels = novelcursor.fetchall()
    for novel in novels:
        #SETUP: define sql, get online chapters and database chapters
        novel_obj = get_HTML(novel[1])
        chapter_sql = "SELECT novelid,chapternumber,section FROM chapters WHERE novelid = %s ORDER BY chapternumber"
        novel_sql = "UPDATE novels SET completed = 'completed' WHERE novelid=%s"
        novelid = (novel[0],)
        novelcursor.execute(chapter_sql,novelid)
        chapters = novelcursor.fetchall()
        chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])

        #check if there are more chapters on NCODE than database; if so, get newest chapter in database than call processChapters
        if len(chapter_list) > len(chapters):
            chapter_list = chapter_list[len(chapters):]
            last_chapter = chapters[-1]
            chapter_number = last_chapter[1]+1
            section = last_chapter[2]
            processChapters(chapter_number=chapter_number,section=section,novel_id=novelid[0],chapter_list=chapter_list)

        #if completed element found on info page set novel to completed
        o = get_HTML(novel[1][:25]+'/novelview/infotop/ncode'+novel[1][25:])
        if o.find(id='noveltype'):
            novelcursor.execute(novel_sql,novelid)
        noveldb.commit()
def upload():#change permissions for viewing of novels
    now = pytz.timezone('America/Los_Angeles')
    now = datetime.datetime.now(now).replace(microsecond=0)
    novel_sql = 'SELECT DISTINCT novel FROM Schedule WHERE day LIKE %s AND time = %s'
    novel_val = (now.strftime("%A"),now.strftime("%H"))
    chapter_sql =  '''
                   UPDATE chapters SET chapteractive = chapteractive-1, date = %s
                   WHERE novelid = %s AND chapteractive = %s ORDER BY chapterorder+0 LIMIT 1;
                   SELECT ISNULL(content) FROM chapters WHERE novelid = %s AND chapteractive = %s LIMIT 1
                   '''

    new_novel_sql = """
                    UPDATE chapters SET chapteractive = 4 LIMIT 5;
                    UPDATE chapters SET chapteractive = 3 LIMIT 3;
                    UPDATE chapters SET chapteractive = 2 LIMIT 2;
                    UPDATE chapters SET chapteractive = 1 Limit 1;
                    """
    novelcursor.execute(novel_sql,novel_val)
    print(now)
    i=5
    try:
        novel = novelcursor.fetchone()[0]
        new_chapter=None
        while i > 1:
            print('index:',i)
            chapter_val = (now,novel,i,novel,i-1)
            for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
                if result.with_rows:
                    try:
                        is_title = novelcursor.fetchall()[0][0]
                        print('title:',is_title)
                        if is_title==0:i-=1 #if content isNULL don't move on
                    except IndexError:
                        print('error')
                        continue
                noveldb.commit()
        #botupload(new_chapter)
    except TypeError:
        print('no uploads now')

#download('https://ncode.syosetu.com/n9303hk/',['Action','Comedy'],['Calm Protagonist','Charming Protagonist'])
def processView(views):
    if views > 1000000:
        processed_views = views%1000000 + 'M'
    elif views > 1000:
        procsesed_views = views%1000 + 'K'
    else:
        processed_views = views
    return processed_views
def ranker(rank):
    rank_digit = rank%10
    if rank > 100:
        return 'N/A'
    elif rank_digit == 1 and rank != 11:
        return str(rank)+'st'
    elif rank_digit == 2 and rank !=12:
        return str(rank)+'nd'
    elif rank_digit == 3 and rank !=13:
        return str(rank)+'rd'
    else:
        return str(rank)+'th'

