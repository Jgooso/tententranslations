import mysql.connector
#downloading novels and chapters
import string, random
import re, requests
#import language_tool_python
from bs4 import BeautifulSoup
from googletrans import Translator
from scripts.settings import DevConfig,ProdConfig
from datetime import datetime,date,timedelta
#Basic intialializations
translator = Translator()
config = DevConfig.SQL_SETTINGS
#Commonly used Functions
def translate(text):#Translate text
    return translator.translate(text).text

def get_HTML(URL):#retrieve HTML from webpage
    response = requests.get(URL,headers={'User-Agent':'Mozilla/5.0'}).text
    return BeautifulSoup(response, 'html.parser')

def distance_from_thousand(elem):#sort function for translations
    return elem%1000

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
    text = text.replace('</p>','')
    text = text.replace('</br>','\n')
    text = text.replace('</ br>','\n')
    text = text.replace('<br/>','\n')
    clean = re.compile('<p id=".*">')
    text = re.sub(clean,'',text)
    clean = re.compile('((<rp|<rt|<ru|</r|<r).*?(/rp>|/rt>|by>|b>))|')
    return re.sub(clean,'',text)
def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def download(data):#download novels from NCODE.SYOSETU
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True)
    #Parse form in data
    genres=[]
    tags=[]
    url=''
    novelstatus='nCompleted'
    image = None
    for d in data:
        if 'genre' in d:
            genres.append(data[d])
        if 'tag' in d:
            tags.append(data[d])
        if d=='url':
            URL=data[d]
        if d=='novelstatus':
            novelstatus='n'+data[d]
    #Retrieve elements from webpage
    novel_obj = get_HTML(URL)
    jp_title = novel_obj.title.text
    en_title = translate(jp_title)
    novel_id = ran_gen(7)
    release = novel_obj.find(class_='long_update').text.strip()[:4]
    author = scrub_HTML(translate(novel_obj.find(class_ = "novel_writername").text)[8:])
    description = scrub_HTML(translate(novel_obj.find(id = 'novel_ex').text.replace('<br />','&#013;&#010;   ')))
    
    #INSERT data into database
    novel_insert_sql =  """INSERT INTO novels(novelid,title,alternativetitle,url,description,novelactive) 
                                       VALUES(%s,%s,%s,%s,%s,%s);
                        """
    novel_insert_val = (
        novel_id,#novelid
        en_title,#title
        jp_title,#alternativetitle
        URL,#url
        description,#description
        0,#novelactive
    )
    #execute sql and retriece id
    novelcursor.execute(novel_insert_sql,novel_insert_val)
    #Get list of all identifiers
    identifiers = genres + tags + [author,release,novelstatus,'uUnreleased']
    for d in identifiers:
        if(d == author):
            novelcursor.execute("REPLACE INTO identifiers (descriptor,type) VALUES (%s,%s)",(author,'authors'))
        descriptor_insert_sql = "INSERT INTO noveldescriptors (novelid,descriptor) SELECT %s,id FROM identifiers WHERE descriptor = %s"
        descriptor_insert_val = (novel_id,d.strip())
        novelcursor.execute(descriptor_insert_sql,descriptor_insert_val)

    #Upload Chapters
    chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
    processChapters(chapter_number=1,section=0,chapter_list=chapter_list,novel_id=novel_id,chaptercursor=novelcursor)
    
    noveldb.commit()
    noveldb.close()
def processChapters(chapter_number,section,novel_id,chapter_list,chaptercursor):#Translates chapters and processes them to be easier to read
    sql = "INSERT INTO chapters (novelid,title,section,chapternumber,content,chapteredited,chapteractive,chapterorder) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    chapter_order = chapter_number+section
    for i in range(len(chapter_list)):
        current_chapter = chapter_list[i]
        print(chapter_order)
        if 'class' in str(current_chapter):
            section+=1
            val = (
                novel_id,#novelid
                translate(current_chapter.text),#title
                section,#section
                0,#chapternumber
                None,#content
                0,#chapteredited
                0,#chapteractive
                chapter_order,#chapterorder
            )
            chaptercursor.execute(sql,val)
        else:
            chapter_obj = get_HTML('https://ncode.syosetu.com' + str(current_chapter['href']))
            chapter_title = translate(str(chapter_obj.find(class_ = 'novel_subtitle').text))
            content = ''
            text = str(chapter_obj.find(id = 'novel_honbun'))[42:-6]
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
            val = (
                novel_id,#novelid
                chapter_title,#chaptertitle
                section,#section
                chapter_number,#chapternumber
                content,#content
                0,#chapteredited
                0,#chapteractive
                chapter_order,#chapterorder
            )
            chaptercursor.execute(sql,val)
            chapter_number += 1
        chapter_order += 1
def processView(views):
    if views == None:
        return 0
    if views >= 1000000:
        processed_views = str(views//1000000) + 'M'
    elif views >= 1000:
        processed_views = str(views//1000) + 'K'
    else:
        processed_views = views
    return processed_views

def time_difference(date):
    current_time = datetime.now().replace(microsecond=0)
    try:
        seconds = (current_time-date.replace(microsecond=0)).total_seconds()
    except:
        return 'unreleased'
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    days = int(hours / 24)
    if seconds < 60 and seconds > 0:
        return str(int(seconds))+' seconds ago'
    elif seconds < 0:
        return 'unreleased'
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

#UNUSED METHODS

#def update():#Search for new chapters and download them to database
#    noveldb = mysql.connector.connect(**config)
#    novelcursor = noveldb.cursor(buffered=True)
#    today = date.today()
#    yesterday = today  - timedelta(days = 1)
#    novelcursor.execute("SELECT id,url,novelstatus FROM novels")
#    novels = novelcursor.fetchall()
#    for novel in novels:
#        #SETUP: define sql, get online chapters and database chapters
#        novel_obj = get_HTML(novel[1])
#        chapter_sql = "SELECT novelid,id,chapternumber,section,views,chapteractive FROM chapters WHERE novelid = %s ORDER BY chapternumber"
#        novel_sql = "UPDATE noveldescriptors SET descriptor = 'completed' WHERE novelid=%s AND descriptor in ('Ongoing','On Hold','Dropped')"
#        data_sql = "INSERT INTO data (novelid,id,views,date) VALUES (%s,%s,%s,%s)"
#        novelid = (novel['id'],)
#        novelcursor.execute(chapter_sql,novelid)
#        chapters = novelcursor.fetchall()
#        chapter_list = novel_obj.find(class_ = 'index_box').find_all(['a','div'])
#        #check if there are more chapters on NCODE than database; if so, get newest chapter in database than call processChapters
#        if len(chapter_list) > len(chapters) and (novel['novelstatus'] == 'Ongoing' or novel['novelstatus'] == 'On Hold'):
#            chapter_list = chapter_list[len(chapters):]
#            last_chapter = chapters[-1]
#            chapter_number = last_chapter['chapternumber']+1
#            section = last_chapter['section']
#            processChapters(chapter_number=chapter_number,section=section,novel_id=novel['id'],chapter_list=chapter_list)
#        for chapter in chapters:
#            if chapter['chapternumber'] != 0 and chapter['chapteractive'] == 1:
#                try:
#                    novelcursor.execute("SELECT views from data WHERE chapterid = %s AND novelid = %s AND date = %s",(chapter['id'],novel['id'],yesterday  - timedelta(days = 1)))
#                    yesterday_views = novelcursor.fetchone()
#                    views = chapter['views']-yesterday_views
#                except TypeError:
#                    views = chapter[-2]
#                data_val = (novel[0],chapter[1],views,yesterday)
#                novelcursor.execute(data_sql,data_val)
#        #if completed element found on info page set novel to completed
#        o = get_HTML(novel[1][:25]+'/novelview/infotop/ncode'+novel[1][25:])
#        if o.find(id='noveltype'):
#            novelcursor.execute(novel_sql,novelid)
#        if today.strftime('%d') == '01':
#            novelcursor.execute('UPDATE chapters SET views = 0')
#    noveldb.commit()
#    noveldb.close()


#def upload_image(image,url):
#    response = requests.get(image)
#    local_filename = image.split('/')[-1]
#    totalbits = 0
#    print(image)
#    if response.status_code == 200:
#        with open('/assets/'+url, 'wb') as f:
#            for chunk in response.iter_content(chunk_size=1024):
#                if chunk:
#                    totalbits += 1024
#                    print("Downloaded",totalbits*1025,"KB...")
#                    f.write(chunk)
#    
#    return url

#def ranker(rank):
#    rank_digit = rank%10
#    if rank > 100:
#        return 'N/A'
#    elif rank_digit == 1 and rank != 11:
#        return str(rank)+'st'
#    elif rank_digit == 2 and rank !=12:
#        return str(rank)+'nd'
#    elif rank_digit == 3 and rank !=13:
#        return str(rank)+'rd'
#    else:
#        return str(rank)+'th'