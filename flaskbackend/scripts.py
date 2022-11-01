import mysql.connector
#downloading novels and chapters
import re
import requests
from slugify import slugify
import language_tool_python
from bs4 import BeautifulSoup
from googletrans import Translator
import json

#uploading chapters to weboage
from datetime import datetime,date,timedelta
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

def get_HTML(URL):#retrieve HTML from webpage
    response = requests.get(URL,headers={'User-Agent':'Mozilla/5.0'}).text
    return BeautifulSoup(response, 'html.parser')

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
                my_new_text[i]=''
     
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
def time_difference(date):
    current_time = datetime.now().replace(microsecond=0)
    try:
        seconds = (current_time-date.replace(microsecond=0)).total_seconds()
    except:
        return 'unreleased'
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    days = int(hours / 24)
    if seconds < 60:
        return str(int(seconds))+' seconds ago'
    elif minutes < 60:
        if minutes == 1:
            return str(minutes)+' minute ago'
        else:
            return str(minutes)+' minutes ago'
    elif hours < 24:
        if hours == 1:
            return str(hours)+' hour ago'
        else:
            return str(hours)+' hours ago'
        
    elif days < 7:
        if days == 1:
            return str(days)+' day ago'
        else:
            return str(days)+' days ago'
    else:
        return date.date().strftime("%d %B, %Y")
def remove_html_tags(text):
    text = text.replace('</p>','\n')
    text = text.replace('</br>','\n')
    text = text.replace('</ br>','\n')
    text = text.replace('<br/>','\n')
    clean = re.compile('(<rp|<rt|<ru|</ru).*(/rp>|/rt>|by>)')
    return re.sub(clean,'',text)

def upload_image(image,url):
    response = requests.get(image)
    local_filename = image.split('/')[-1]
    totalbits = 0
    print(image)
    if response.status_code == 200:
        with open('/assets/'+url, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    totalbits += 1024
                    print("Downloaded",totalbits*1025,"KB...")
                    f.write(chunk)
    
    return url

def download(URL,genres,tags,image):#download novels from NCODE.SYOSETU
    #Retrieve elements from webpage
    novel_obj = get_HTML(URL)
    jp_title = novel_obj.title.text
    en_title = translate(jp_title)
    novel_id = slugify(en_title.replace("'",""))
    release = novel_obj.find(class_='long_update').text.strip()[:4]
    author = scrub_HTML(translate(novel_obj.find(class_ = "novel_writername").text)[8:])
    description = scrub_HTML(correct_grammer(translate(novel_obj.find(id = 'novel_ex').text.replace('<br />','&#013;&#010;   '))))
    
    #INSERT data into database
    novel_insert_sql =  """INSERT INTO novels(novelid,title,alternativetitle,url,description,novelactive) 
                                       VALUES(%s,%s,%s,%s,%s,%s);
                          SELECT id FROM novels WHERE novelid = %s
                        """
    novel_insert_val = (
        novel_id,#novelid
        en_title,#title
        jp_title,#alternativetitle
        URL,#url
        description,#description
        0,#novelactive
        novel_id#select id,
    )
    #execute sql and retriece id
    for result in novelcursor.execute(novel_insert_sql,novel_insert_val,multi=True):
            if result.with_rows:
                novel_identifier = novelcursor.fetchone()[0]
    
    #Get list of all identifiers
    identifiers = genres + tags.split(',') + [author,release,'nOngoing','uUnreleased']
    for d in identifiers:
        if(d == author):
            novelcursor.execute("REPLACE INTO identifiers (descriptor,type) VALUES (%s,%s)",(author,'authors'))
        descriptor_insert_sql = "INSERT INTO noveldescriptors (novelid,descriptor) SELECT %s,id FROM identifiers WHERE descriptor = %s"
        descriptor_insert_val = (novel_identifier,d.strip())
        print(d.strip())
        novelcursor.execute(descriptor_insert_sql,descriptor_insert_val)


    #Upload Chapters
    chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
    processChapters(chapter_number=1,section=0,chapter_list=chapter_list,novel_id=novel_identifier)

    #Upload IMAGE
    
    noveldb.commit()

def processChapters(chapter_number,section,novel_id,chapter_list):#Translates chapters and processes them to be easier to read
    sql = "INSERT INTO chapters (novelid,title,section,chapternumber,content,chapteractive,chapterorder,views) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    chapter_order = chapter_number+section
    for i in range(len(chapter_list)):
        print(chapter_number)
        current_chapter = chapter_list[i]
        if 'class' in str(current_chapter):
            section+=1
            val = (
                novel_id,#novelid
                translate(current_chapter.text),#title
                section,#section
                 0,#chapternumber
                None,#content
                1,#active
                chapter_order,#chapterorder
                0,#views
            )
            novelcursor.execute(sql,val)
        else:
            chapter_obj = get_HTML('https://ncode.syosetu.com' + str(current_chapter['href']))
            chapter_title = translate(str(chapter_obj.find(class_ = 'novel_subtitle').text))
            content = ''
            text = '   '+'   '.join([str(p)[str(p).index('>')+1:] for p in chapter_obj.find(id = 'novel_honbun').find_all("p")])
            #process text content
            text = remove_html_tags(text)
            #find good points of division
            new_lines=[_.start() for _ in re.finditer('\n', text)]
            divide_index={0:0}
            for line in new_lines:
                if line//1000 !=0:
                    if line//1000 not in divide_index:
                        divide_index[line//1000] = line
                    if line < divide_index[line//1000]:
                        divide_index[line//1000] = line
            if len(text) - divide_index[len(divide_index)-1] < 100:
                divide_index[len(divide_index)-1] = len(text)
            else:
                divide_index[len(divide_index)]=len(text)
            divider = [v for (k,v) in divide_index.items()]

            #translate and grammer check chapters
            for j in range(len(divider)-1):
                content += translate(text[divider[j]:divider[j+1]])
            content = scrub_HTML(content)
            content = correct_grammer(content)
            val = (
                novel_id,#novelid
                chapter_title,#chaptertitle
                section,#section
                chapter_number,#chapternumber
                content,#content
                1,#chapteractive
                chapter_order,#chapterorder
                0,#views

            )
            novelcursor.execute(sql,val)
            chapter_number += 1
        chapter_order += 1

def update():#Search for new chapters and download them to database
    today = date.today()
    yesterday = today  - timedelta(days = 1)
    novelcursor.execute("SELECT id,url,novelstatus FROM novels")
    novels = novelcursor.fetchall()
    for novel in novels:
        #SETUP: define sql, get online chapters and database chapters
        novel_obj = get_HTML(novel[1])
        chapter_sql = "SELECT novelid,chapterid,chapternumber,section,views,chapteractive FROM chapters WHERE novelid = %s ORDER BY chapternumber"
        novel_sql = "UPDATE noveldescriptors SET descriptor = 'completed' WHERE novelid=%s AND descriptor in ('Ongoing','On Hold','Dropped')"
        data_sql = "INSERT INTO data (novelid,chapterid,views,date) VALUES (%s,%s,%s,%s)"
        novelid = (novel['id'],)
        novelcursor.execute(chapter_sql,novelid)
        chapters = novelcursor.fetchall()
        chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
        #check if there are more chapters on NCODE than database; if so, get newest chapter in database than call processChapters
        if len(chapter_list) > len(chapters) and (novel[-1] == 'Ongoing' or novel[-1] == 'On Hold'):
            chapter_list = chapter_list[len(chapters):]
            last_chapter = chapters[-1]
            chapter_number = last_chapter['chapternumber']+1
            section = last_chapter['section']
            processChapters(chapter_number=chapter_number,section=section,novel_id=novelid[0],chapter_list=chapter_list)
        for chapter in chapters:
            if chapter[2] != 0 and chapter[-1] == 0:
                try:
                    novelcursor.execute("SELECT views from data WHERE chapterid = %s AND novelid = %s AND date = %s",(chapter[1],novel[0],yesterday  - timedelta(days = 1)))
                    yesterday_views = novelcursor.fetchone()
                    views = chapter[-2]-yesterday_views
                except TypeError:
                    views = chapter[-2]
                data_val = (novel[0],chapter[1],views,yesterday)
                novelcursor.execute(data_sql,data_val)
        #if completed element found on info page set novel to completed
        o = get_HTML(novel[1][:25]+'/novelview/infotop/ncode'+novel[1][25:])
        if o.find(id='noveltype'):
            
            novelcursor.execute(novel_sql,novelid)
        noveldb.commit()
        if today.strftime('%d') == '01':
            novelcursor.execute('UPDATE chapters SET views = 0')
def upload():#change permissions for viewing of novels
    now = pytz.timezone('America/Chicago')
    check_date = datetime.now(now).replace(microsecond=0)
    current_time = datetime.now().replace(microsecond=0)
    novel_sql = """
                    SELECT DISTINCT schedule.novelid 
                        FROM Schedule 
                            INNER JOIN novels 
                                ON schedule.novelid = novels.novelid 
                    WHERE day LIKE %s AND time = %s AND novels.novelactive = 1
                """
    novel_val = (check_date.strftime("%A"),check_date.strftime("%H"))
    chapter_sql =  """
                   UPDATE chapters SET chapteractive = 1, uploaddate = %s
                   WHERE novelid = %s AND chapteractive = 0 ORDER BY chapterorder+0 LIMIT 1;
                   UPDATE novels SET lastupload = %s WHERE novelid = %s;
                   """
    #SQL NOT EXECUTING FIX
    novelcursor.execute(novel_sql,novel_val)
    print(novel_val)
    check_chapter_sql="SELECT ISNULL(content) FROM chapters WHERE novelid = %s AND chapteractive = 0 LIMIT 1"
    try:
        i=1
        novel = novelcursor.fetchone()[0]
        print(novel)
        check_chapter_val = (novel,)
        chapter_val = (current_time,novel,current_time,novel)
        novelcursor.execute(check_chapter_sql,check_chapter_val)
        if novelcursor.fetchone()[0] == 0: i = 2
        for x in range(i):
            novelcursor.execute(chapter_sql,chapter_val,multi=True)
            noveldb.commit()
    except TypeError:
        pass
        
def processView(views):
    if views >= 1000000:
        processed_views = str(views//1000000) + 'M'
    elif views >= 1000:
        processed_views = str(views//1000) + 'K'
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
