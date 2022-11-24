import datetime
import os
#from jinja2 import Undefined
import mysql.connector
#import json
import pytz
from PIL import Image
from slugify import slugify
from scripts import download, processView, ranker, time_difference
from flask import jsonify, request

#Setup
config = {
'user': 'root',
'password': 'jeg4Iphone',
'host': '127.0.0.1',
'port': '3306',
'database': 'tententranslations',
'raise_on_warnings': True,}

def get_multiplenovels():
    #Retrieve Data from Frontend
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    identifier = request.args.get('identifier').replace('|','&nbsp;')
    tier= request.args.get('tier')
    page = (int(request.args.get('page'))-1)*12
    order = request.args.get('order')
    if order == "views" or order == "length":
        order = order + ' DESC' 
    get_multiple_novel_val = (identifier,tier,tier,page)
    #multiple_novel_sql
    get_multiple_novel_chapter_sql =    """
                                        SELECT chapternumber,uploaddate 
                                        FROM chapters 
                                        WHERE CONTENT IS NOT NULL AND chapteractive <= %s AND novelid = %s 
                                        ORDER BY chapternumber+0 DESC LIMIT 2
                                    """
    if identifier != 'undefined':
        get_multiple_novel_sql = """SELECT novels.id,novels.novelid,novels.title,imageurl,SUM(chapters.views) as views,SUM(character_length(content)) as length
                                FROM novels 
                                    INNER JOIN noveldescriptors 
                                        ON novels.id = noveldescriptors.novelid 
                                    INNER JOIN Chapters
                                        ON novels.id = chapters.novelid
                                    INNER JOIN identifiers
                                        ON noveldescriptors.descriptor = identifiers.id
                                WHERE identifiers.descriptor = %s AND chapteractive <= %s AND novels.novelactive <= %s
                                GROUP BY novels.id
                                ORDER BY """+order+"""
                                LIMIT 12 OFFSET %s
                             """
        novelcursor.execute(get_multiple_novel_sql,get_multiple_novel_val)
    else:
        get_multiple_novel_sql = """SELECT novels.id,novels.novelid,novels.title,imageurl, SUM(chapters.views) as views,SUM(character_length(content)) as length
                                        FROM novels 
                                            INNER JOIN chapters
                                                ON novels.id = chapters.novelid
                                            WHERE novels.novelactive <= %s AND chapteractive <= %s
                                    GROUP BY novels.id
                                    ORDER BY  """+order+"""
                                    LIMIT 12 OFFSET %s
                                """
        novelcursor.execute(get_multiple_novel_sql,(tier,tier,page))
    novelData = novelcursor.fetchall()
    #Add chapters to novelData
    for novel in novelData:
        get_multiple_novel_val = (tier,novel['id'])
        novelcursor.execute(get_multiple_novel_chapter_sql,get_multiple_novel_val)
        chapterResults = novelcursor.fetchall()
        for chapter in chapterResults:
            chapter['uploaddate'] = time_difference(chapter['uploaddate'])
        try:
            novel['firstChapter'] = chapterResults[0]
            novel['secondChapter']=chapterResults[1]
        except IndexError:
           pass
    noveldb.close()
    return jsonify(novelData)

def get_singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    edit = request.args.get('edit')
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        #Retrieve Novel Data
        
        get_single_novel_sql = """SELECT DISTINCT novels.id,novels.novelid,novels.title,alternativetitle,description,url,novelactive, SUM(chapters.views) as views,CEILING(SUM(character_length(content))/1800) as pages 
                        FROM novels 
                            INNER JOIN chapters 
                                ON novels.id = chapters.novelid 
                        WHERE novels.novelid = %s
                        GROUP BY novels.id
                    """
        get_single_novel_val = (novel,)
        novelcursor.execute(get_single_novel_sql,get_single_novel_val)
        novelData=novelcursor.fetchone()
        if novelData:
            novelData['views'] = processView(novelData['views'])
        else:
            return {}

        #Retrieve Chapters
        get_single_novel_chapter_sql = """
                            SELECT title,novelid,uploaddate,chapternumber,section,id,chapterorder 
                                FROM chapters WHERE novelid = %s AND chapteractive <= %s 
                                ORDER BY chapterorder+0
                           """
        get_chapter_list_val = (novelData['id'],tier)
        novelcursor.execute(get_single_novel_chapter_sql,get_chapter_list_val)
        chapter_list = novelcursor.fetchall()
       
        #Retrieve Novel identifiers
        get_single_novel_descriptor_sql = """SELECT identifiers.descriptor,identifiers.type 
                                FROM noveldescriptors 
                                    INNER JOIN identifiers 
                                        ON identifiers.id = noveldescriptors.descriptor 
                                WHERE noveldescriptors.novelid = %s"""
        get_single_novel_descriptor_val = (novelData['id'],)
        novelcursor.execute(get_single_novel_descriptor_sql,get_single_novel_descriptor_val)
        identifiers = novelcursor.fetchall()
        genres = []
        tags = []
        for descriptor in identifiers:
            if descriptor['type'] == 'genre':
                genres.append(descriptor['descriptor'])
            elif descriptor['type'] == 'tag':
                tags.append(descriptor['descriptor'])
            elif descriptor['type'] == 'uploadstatus':
                uploadstatus = descriptor['descriptor'][1:]
            elif descriptor['type'] == 'novelstatus':
                novelstatus = descriptor['descriptor'][1:]
            elif descriptor['type'] == 'novelrelease':
                novelrelease = descriptor['descriptor']
            elif descriptor['type'] == 'authors':
                author = descriptor['descriptor']
        novelData['tags'] = tags
        novelData['genres'] = genres
        novelData['uploadstatus'] = uploadstatus
        novelData['novelstatus'] = novelstatus
        novelData['authors'] = author
        novelData['novelrelease'] = novelrelease
        #Editable get Genres and tags
        if(edit=='True'):
            novelcursor.execute('SELECT * FROM identifiers WHERE type = "tag" OR type = "genre"')
            identifiers = novelcursor.fetchall()
            genres = []
            tags = []
            for d in identifiers:
                if d['type'] == 'tag':
                    tags.append(d['descriptor'])
                elif d['type'] == 'genre':
                    genres.append(d['descriptor'])
        #Return Data
        noveldb.close()
        return jsonify({'Novel':novelData,'Chapters':chapter_list,'Genres':genres,'Tags':tags})
    if request.method == 'POST':#Create Novel
        data = request.form
        download(data=data)
        return data
    if request.method == 'PUT':#Edit Novel
        data = request.get_json()
        novelid = slugify(data['title'])
        post_single_novel_sql =  """
                                UPDATE novels SET description = %s, title = %s, novelid = %s
                                    WHERE novelid = %s;
                                SELECT id FROM novels WHERE novelid = %s
                                 """
        post_single_novel_val = (data['description'],data['title'],novelid,novel,novelid)
        for result in novelcursor.execute(post_single_novel_sql,post_single_novel_val,multi=True):
            if result.with_rows:
                id = novelcursor.fetchone()['id']
        post_single_novel_descriptor_sql = "REPLACE INTO noveldescriptors (novelid,descriptor) SELECT %s,id FROM identifiers WHERE descriptor = %s AND type != 'uploadstatus'"
        for descriptor in data['genres'] + data['tags']+[data['completed']]:
            post_single_novel_descriptor_val = (id,descriptor)
            novelcursor.execute(post_single_novel_descriptor_sql,post_single_novel_descriptor_val)
        noveldb.commit()
        noveldb.close()
        return data
    if request.method == 'DELETE':#Delete Novel
        delete_single_novel_sql = 'DELETE FROM novels WHERE novelid=%s'
        delete_single_novel_val = (novel,)
        novelcursor.execute(delete_single_novel_sql,delete_single_novel_val)
        noveldb.commit()
        noveldb.close() #close the connection
        return 'deleted'
def get_chapter():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    chapter = request.args.get('chapter')
    novel = request.args.get('novel')
    update_chapter = request.args.get('chapterupdate')
    if request.method == 'GET':
        get_chapter_sql = """
                        SELECT DISTINCT content 
                            FROM chapters 
                            WHERE chapternumber = %s AND novelid=%s;
                        UPDATE chapters SET views = views + (1 - chapteractive) 
                            WHERE chapternumber = %s AND novelid = %s
                      """
        get_chapter_val = (chapter,novel,chapter,novel)
        chapter_results = []
        for result in novelcursor.execute(get_chapter_sql,get_chapter_val,multi=True):
            if result.with_rows:
                chapter_results = novelcursor.fetchone()['content']
        noveldb.commit()
        noveldb.close()
        return chapter_results
    if request.method == 'PUT':
        data = request.get_json()
        try:
            put_chapter_sql = 'UPDATE chapters SET content = %s WHERE chapternumber = %s AND novelid = %s'
            put_chapter_val = (data['content'],update_chapter,novel)
            novelcursor.execute(put_chapter_sql,put_chapter_val)
        except:
            print(update_chapter,novel)
            
        put_get_chapter_sql = "SELECT DISTINCT content FROM chapters WHERE chapternumber = %s AND novelid=%s"
        put_get_chapter_val = (chapter,novel)
        novelcursor.execute(put_get_chapter_sql,put_get_chapter_val)
        chapter_data = novelcursor.fetchone()['content']
        noveldb.commit()
        noveldb.close()
        return chapter_data

def get_genres_and_tags():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        novelcursor.execute('SELECT * FROM identifiers WHERE type = "tag" OR type = "genre"')
        identifiers = novelcursor.fetchall()
        genres = []
        tags = []
        for descriptor in identifiers:
            if descriptor['type'] == 'tag':
                tags.append(descriptor['descriptor'])
            elif descriptor['type'] == 'genre':
                genres.append(descriptor['descriptor'])
        noveldb.close()
        return jsonify({'genres':genres, 'tags':tags})
    
def get_schedules():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        start_date = datetime.date(2022, 10, 1) 
        end_date = datetime.date(2022, 10, 30) 
        get_schedule__sql = ('SELECT title,upload_date FROM schedule INNER JOIN novels ON novels.id = schedule.novelid WHERE upload_date BETWEEN %s AND %s')
        get_schedule_val = (start_date,end_date)
        novelcursor.execute(get_schedule__sql,get_schedule_val)
        schedule_list = novelcursor.fetchall()
        
        schedule_bucket = {}
        for schedule in schedule_list:
            day = schedule['upload_date']
            print(day.day,day.hour)
            if day.day not in schedule_bucket:
                schedule_bucket[day.day] = []
            schedule_bucket[day.day].append(day.hour)
        noveldb.close()
        return jsonify(schedule_bucket)
    if request.method == 'POST':
        local = pytz.timezone("America/Chicago")
        data = request.form
        novel = data['novel']
        date = [int(d) for d in data['upload-start'].split('-')]
        start_date = datetime.datetime(date[0],date[1],date[2])
        times = [datetime.time(int(data[t][:2])) for t in data if 'time' in t]
        days_of_the_week = [int(data[w]) for w in data if 'day' in w]
        dates = []
        novelcursor.execute('SELECT COUNT(content) as length FROM chapters INNER JOIN novels ON chapters.novelid = novels.id WHERE novels.novelid = %s',(novel,))
        length = novelcursor.fetchone()['length']
        print(length)
        i = 0
        while len(dates) < length:
            day = start_date + datetime.timedelta(days=i)
            print(day,((day.weekday()+1)%7))
            if (day.weekday()+1)%7 in days_of_the_week:
                for t in times:
                    dates.append(datetime.datetime.combine(day,t).astimezone(local))
                    if len(dates) >= length:
                        break

            if(i > 100):
                break
            i+=1
        print(len(dates))
        for d in dates:
            d = d.astimezone(pytz.UTC)
            print('utc:'+d.strftime("%Y-%m-%d, %H:%M"))
            novelcursor.execute("INSERT INTO schedule (upload_date,novelid) SELECT %s,id FROM novels WHERE novelid = %s",(d,novel))
        noveldb.commit()
        noveldb.close()
        return data

def get_noveltitles():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        novelcursor.execute("""
                                SELECT title,novels.novelid,id
                                    FROM novels 
                                    
                            """)
        novels = novelcursor.fetchall()
        noveldb.close()
        return jsonify(novels)

def get_user():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        user_id = request.args.get('userID')
        novelcursor.execute("SELECT * FROM users WHERE id = %s",(user_id,))
        user = novelcursor.fetchone()
        print(user_id)
        noveldb.close()
        return jsonify(user)
    if request.method == 'POST':
        data = request.get_json()
        user_id = data['userID']
        print(user_id)
        novelcursor.execute('INSERT INTO users(id) VALUES (%s)',(user_id,))
        noveldb.commit()
        noveldb.close()
        return str(user_id)
def get_home_page_novels():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    tier= request.args.get('tier')
    if request.method == 'GET':
        get_multiple_novel_chapter_sql =    """
                                        SELECT chapternumber,uploaddate 
                                        FROM chapters 
                                        WHERE CONTENT IS NOT NULL AND chapteractive <= %s AND novelid = %s 
                                        ORDER BY chapternumber+0 DESC LIMIT 2
                                    """
        home_page_popular_sql = """
                                SELECT novels.id,novels.novelid,novels.title,imageurl,novelactive,description,sum(chapters.views) as views,ROW_NUMBER() OVER (ORDER BY sum(chapters.views) DESC) row_num,ANY_VALUE(genre.des) as genre
                                FROM novels INNER JOIN chapters ON chapters.novelid = novels.id
                                LEFT JOIN (
                                        SELECT identifiers.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN identifiers ON noveldescriptors.descriptor = identifiers.id
                                            WHERE type = 'genre'
                                            ORDER BY identifiers.descriptor
                                    ) AS genre
                                        ON genre.nov = novels.id
                                    WHERE novelactive <= %s
                                    GROUP BY novels.id
                                    ORDER BY views DESC
                                    LIMIT 9;
                            """
        home_page_recent_sql =  """
                                SELECT novels.id,title,novels.novelid,imageurl,ANY_VALUE(genre.des) AS genre,novelactive FROM novels 
                                    LEFT JOIN (
                                        SELECT identifiers.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN identifiers ON noveldescriptors.descriptor = identifiers.id
                                            WHERE type = 'genre'
                                            ORDER BY identifiers.descriptor
                                    ) AS genre
                                        ON genre.nov = novels.id
                                    WHERE novelactive <= %s
	                                GROUP BY novels.id
                                    ORDER BY firstupload
                                    LIMIT 7;
                            """
        home_page_latest_sql =  """
                                SELECT novels.id,title,novels.novelid,imageurl,ANY_VALUE(genre.des) AS genre,novelactive FROM novels 
                                    LEFT JOIN (
                                        SELECT identifiers.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN identifiers ON noveldescriptors.descriptor = identifiers.id
                                            WHERE type = 'genre'
                                            ORDER BY identifiers.descriptor
                                    ) AS genre
                                        ON genre.nov = novels.id
                                    WHERE novelactive <= %s
	                                GROUP BY novels.id
                                    ORDER BY lastupload
                                    LIMIT 7;
                            """
        tier_val = (tier,)
        novelcursor.execute(home_page_popular_sql,tier_val)
        popular_novels = novelcursor.fetchall()
        novelcursor.execute(home_page_recent_sql,tier_val)
        recent_novels = novelcursor.fetchall()
        novelcursor.execute(home_page_latest_sql,tier_val)
        latest_novels = novelcursor.fetchall()
        for novel in recent_novels+latest_novels:
            get_multiple_novel_val = (tier,novel['id'])
            novelcursor.execute(get_multiple_novel_chapter_sql,get_multiple_novel_val)
            chapterResults = novelcursor.fetchall()
            for chapter in chapterResults:
                chapter['uploaddate'] = time_difference(chapter['uploaddate'])
            novel['firstChapter'] = chapterResults[0]
            try:
                novel['secondChapter']=chapterResults[1]
            except IndexError:
                pass
            
        noveldb.close()
        return jsonify({'popular':popular_novels,'recent':recent_novels,'latest':latest_novels})

def get_feedback():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        page= int(request.args.get('page'))
        novelcursor.execute("SELECT * FROM feedback LIMIT 5 OFFSET %s",(page,))
        feedback_list = novelcursor.fetchall()
        noveldb.close()
        return jsonify(feedback_list)
    if request.method == 'POST':
        feedback = request.get_json()['feedback']
        novelcursor.execute("INSERT INTO feedback(feedback) VALUES (%s)",(feedback,))
        noveldb.commit()
        noveldb.close()
        return 'posted'
    if request.method == 'DELETE':
        id= request.args.get('id')
        novelcursor.execute("DELETE FROM feedback WHERE id = %s",(id,))
        noveldb.close()
        return 'deleted'
def get_novels_page_count():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    tier= request.args.get('tier')
    identifier = request.args.get('identifier').replace('|','&nbsp;')
    tier= request.args.get('tier')
    if request.method == 'GET':
        if identifier != 'undefined':
            novelcursor.execute("""SELECT COUNT(novels.novelid) as count FROM novels 
                                    INNER JOIN noveldescriptors 
                                        ON novels.id = noveldescriptors.novelid 
                                    INNER JOIN identifiers
                                        ON noveldescriptors.descriptor = identifiers.id
                                    WHERE novelactive <= %s AND 
                                        identifiers.descriptor = %s
                                        
                                """,(tier,identifier))
        else:
             novelcursor.execute("SELECT COUNT(novelid) as count FROM novels WHERE novelactive <= %s",(tier,) )
        novel_count = (int(novelcursor.fetchone()['count']))
        page_count = ((novel_count)//12)+1
        print(page_count)
        noveldb.close()
        return {'page_count':page_count,'novel_count':novel_count}

#ADD REMAINING FILE SIZE

def get_dates():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        offset= int(request.args.get('offset'))
        start_date = datetime.date(2022, 10, 1) 
        end_date = datetime.date(2022, 10, 31) 
        #start_date = start_date - datetime.timedelta(days=(start_date.weekday()+1)%7)
        #print(start_date)
        delta = end_date - start_date   # returns timedelta
        october_calender = {'month':'October','weekday_start':(start_date.weekday()+1)%7,'days':{}}
        get_schedule__sql = ('SELECT title,upload_date FROM schedule INNER JOIN novels ON novels.id = schedule.novelid WHERE upload_date BETWEEN %s AND %s')
        get_schedule_val = (start_date,end_date)
        novelcursor.execute(get_schedule__sql,get_schedule_val)
        schedule_list = novelcursor.fetchall()
        schedule_bucket = {}
        for schedule in schedule_list:
            day = schedule['upload_date'] - datetime.timedelta(minutes=offset)
            if day.day not in schedule_bucket:
                schedule_bucket[day.day] = []
            schedule_bucket[day.day].append({'novel':schedule['title'],'hour':day.hour})
        for i in range(delta.days + 1):
            day = start_date + datetime.timedelta(days=i)
            october_calender['days'][day.day] = []
            try:
                for d in schedule_bucket[day.day]:
                    october_calender['days'][day.day].append(d)
            except:
                pass
        noveldb.close()
        return jsonify(october_calender)
def testing():
    if request.method=='POST':
        print(request.form)
        print(request.files)
        file_name = request.files['file'].filename
        file = convertToBinaryData(request.files['file'])
        print(os.listdir('./static'))
       
        with open(os.path.join('./static/assets',file_name),'wb') as f:
            f.write(file)
        return request.method
def get_database_size():
    if request.method == 'GET':
       pass

def convertToBinaryData(file):
    # Convert digital data to binary format
    binaryData = file.read()
    return binaryData