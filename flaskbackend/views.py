import datetime
from operator import indexOf

from jinja2 import Undefined
import mysql.connector
import json
from slugify import slugify
from scripts import download, processView, ranker, time_difference
from flask import Flask, jsonify, request, session

#Setup
config = {
'user': 'root',
'password': 'jeg4Iphone',
'host': '127.0.0.1',
'port': '3306',
'database': 'tententranslations',
'raise_on_warnings': True,}
noveldb = mysql.connector.connect(**config)
novelcursor = noveldb.cursor(buffered=True,dictionary=True)

def get_multiplenovels():
    #Retrieve Data from Frontend
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    try:
        category = request.args.get('category')[request.args.get('category').index('-')+1:]
    except ValueError:
        category = request.args.get('category')
    identifier = request.args.get('identifier').replace('|','&nbsp;')
    tier= request.args.get('tier')
    get_multiple_novel_val = (identifier,tier,tier)

    #multiple_novel_sql
    get_multiple_novel_chapter_sql =    """
                                        SELECT chapternumber,uploaddate 
                                        FROM chapters 
                                        WHERE CONTENT IS NOT NULL AND chapteractive <= %s AND novelid = %s 
                                        ORDER BY chapternumber+0 DESC LIMIT 2
                                    """
    if category != 'undefined':
        get_multiple_novel_sql = """SELECT novels.id,novels.novelid,novels.title,lastupload,firstupload,imageurl,SUM(chapters.views) as views
                                FROM novels 
                                    INNER JOIN noveldescriptors 
                                        ON novels.id = noveldescriptors.novelid 
                                    INNER JOIN Chapters
                                        ON novels.id = chapters.novelid
                                    INNER JOIN descriptors
                                        ON noveldescriptors.descriptor = descriptors.id
                                WHERE descriptors.descriptor = %s AND chapteractive <= %s AND novels.novelactive <= %s
                                GROUP BY novels.id
                             """
        novelcursor.execute(get_multiple_novel_sql,get_multiple_novel_val)
    else:
        get_multiple_novel_sql = """SELECT novels.id,novels.novelid,novels.title,lastupload,firstupload,imageurl, SUM(chapters.views) as views 
                                        FROM novels 
                                            INNER JOIN chapters
                                                ON novels.id = chapters.novelid
                                            WHERE novels.novelactive <= %s AND chapteractive <= %s
                                    GROUP BY novels.id
                                """
        novelcursor.execute(get_multiple_novel_sql,(tier,tier))
    novelData = novelcursor.fetchall()
    print(tier)
    #Add chapters to novelData
    for novel in novelData:
        get_multiple_novel_val = (tier,novel['id'])
        novelcursor.execute(get_multiple_novel_chapter_sql,get_multiple_novel_val)
        chapterResults = novelcursor.fetchall()
        if(novel['lastupload']):
            novel['lastupload'] = novel['lastupload'].isoformat()
        for chapter in chapterResults:
            chapter['uploaddate'] = time_difference(chapter['uploaddate'])
        try:
            novel['firstChapter'] = chapterResults[0]
            novel['secondChapter']=chapterResults[1]
        except IndexError:
           pass
        print(novel['lastupload'])
    return jsonify(novelData)

def get_singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    edit = request.args.get('edit')
    if request.method == 'GET':
        #Retrieve Novel Data
        get_single_novel_sql = """SELECT DISTINCT novels.id,novels.novelid,novels.title,alternativetitle,description,url,novelactive, SUM(chapters.views) as views 
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
       
        #Retrieve Novel Descriptors
        get_single_novel_descriptor_sql = """SELECT descriptors.descriptor,descriptors.type 
                                FROM noveldescriptors 
                                    INNER JOIN descriptors 
                                        ON descriptors.id = noveldescriptors.descriptor 
                                WHERE noveldescriptors.novelid = %s"""
        get_single_novel_descriptor_val = (novelData['id'],)
        novelcursor.execute(get_single_novel_descriptor_sql,get_single_novel_descriptor_val)
        descriptors = novelcursor.fetchall()
        genres = []
        tags = []
        for descriptor in descriptors:
            if descriptor['type'] == 'genre':
                genres.append(descriptor['descriptor'])
            elif descriptor['type'] == 'tag':
                tags.append(descriptor['descriptor'])
            elif descriptor['type'] == 'uploadstatus':
                uploadstatus = descriptor['descriptor']
            elif descriptor['type'] == 'novelstatus':
                novelstatus = descriptor['descriptor']
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
            novelcursor.execute('SELECT * FROM descriptors WHERE type = "tag" OR type = "genre"')
            descriptors = novelcursor.fetchall()
            genres = []
            tags = []
            for d in descriptors:
                if d['type'] == 'tag':
                    tags.append(d['descriptor'])
                elif d['type'] == 'genre':
                    genres.append(d['descriptor'])
        #Return Data
        return jsonify({'Novel':novelData,'Chapters':chapter_list,'Genres':genres,'Tags':tags})
    if request.method == 'POST':#Create Novel
        data = request.get_json()
        input_tags = ','.join(data['tags'])
        input_genres = data['genres']
        input_url = data['url']
        print(input_url)
        download(URL=input_url,tags=input_tags,genres=input_genres)
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
        post_single_novel_descriptor_sql = "REPLACE INTO noveldescriptors (novelid,descriptor) SELECT %s,id FROM descriptors WHERE descriptor = %s AND type != 'uploadstatus'"
        for descriptor in data['genres'] + data['tags']+[data['completed']]:
            post_single_novel_descriptor_val = (id,descriptor)
            novelcursor.execute(post_single_novel_descriptor_sql,post_single_novel_descriptor_val)

        noveldb.commit()
        return data
    if request.method == 'DELETE':#Delete Novel
        delete_single_novel_sql = 'DELETE FROM novels WHERE novelid=%s'
        delete_single_novel_val = (novel,)
        novelcursor.execute(delete_single_novel_sql,delete_single_novel_val)
        noveldb.commit()

def get_chapter():
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
        return chapter_data

def get_genres_and_tags():
    if request.method == 'GET':
        novelcursor.execute('SELECT * FROM descriptors WHERE type = "tag" OR type = "genre"')
        descriptors = novelcursor.fetchall()
        genres = []
        tags = []
        for descriptor in descriptors:
            if descriptor['type'] == 'tag':
                tags.append(descriptor['descriptor'])
            elif descriptor['type'] == 'genre':
                genres.append(descriptor['descriptor'])
        return jsonify({'genres':genres, 'tags':tags})
    
def get_schedules():
    if request.method == 'GET':
        novel = request.args.get('novel')
        get_schedule__sql = ('SELECT * FROM schedule INNER JOIN novels ON novels.id = schedule.novelid WHERE novels.novelid = %s')
        get_schedule_val = (novel,)
        novelcursor.execute(get_schedule__sql,get_schedule_val)
        schedule_list = novelcursor.fetchall()
        schedule_bucket = {}
        for schedule in schedule_list:
            if schedule['day'] not in schedule_bucket:
                schedule_bucket[schedule['day']] = []
            schedule_bucket[schedule['day']].append(schedule)

        return jsonify(schedule_bucket)
    if request.method == 'POST':
        data = request.get_json()
        input_novel = data['novel']
        input_time = data['time'][:2]
        input_dates = data['dates']
        print(input_novel,input_time,input_dates)
        for date in input_dates:
            post_schedule_sql = 'INSERT INTO schedule (time,day,novelid) SELECT %s,%s,id FROM novels WHERE novelid = %s'
            post_schedule_val = (input_time,date,input_novel)
            novelcursor.execute(post_schedule_sql,post_schedule_val)
            print(date)
        noveldb.commit()
        return data

def get_noveltitles():
    if request.method == 'GET':
        novelcursor.execute("""
                                SELECT title,novels.novelid,id
                                    FROM novels 
                                    INNER JOIN noveldescriptors 
                                        ON novels.id = noveldescriptors.novelid 
                                WHERE descriptor in (220,507,509)
                            """)
        novels = novelcursor.fetchall()
        return jsonify(novels)

def get_user():
    if request.method == 'GET':
        user_id = request.args.get('userID')
        novelcursor.execute("SELECT * FROM users WHERE id = %s",(user_id,))
        user = novelcursor.fetchone()
        print(user_id)
        return jsonify(user)
    if request.method == 'POST':
        data = request.get_json()
        user_id = data['userID']
        print(user_id)
        novelcursor.execute('INSERT INTO users(id) VALUES (%s)',(user_id,))
        noveldb.commit()
        return str(user_id)
def get_home_page_novels():
    tier= request.args.get('tier')
    if request.method == 'GET':
        get_multiple_novel_chapter_sql =    """
                                        SELECT chapternumber,uploaddate 
                                        FROM chapters 
                                        WHERE CONTENT IS NOT NULL AND chapteractive <= %s AND novelid = %s 
                                        ORDER BY chapternumber+0 DESC LIMIT 2
                                    """
        home_page_popular_sql = """
                                SELECT novels.id,novels.novelid,novels.title,imageurl,novelactive,description,sum(chapters.views) as views,ANY_VALUE(genre.des) as genre
                                FROM novels INNER JOIN chapters ON chapters.novelid = novels.id
                                LEFT JOIN (
                                        SELECT descriptors.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN descriptors ON noveldescriptors.descriptor = descriptors.id
                                            WHERE type = 'genre'
                                            ORDER BY descriptors.descriptor
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
                                        SELECT descriptors.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN descriptors ON noveldescriptors.descriptor = descriptors.id
                                            WHERE type = 'genre'
                                            ORDER BY descriptors.descriptor
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
                                        SELECT descriptors.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN descriptors ON noveldescriptors.descriptor = descriptors.id
                                            WHERE type = 'genre'
                                            ORDER BY descriptors.descriptor
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
            

        return jsonify({'popular':popular_novels,'recent':recent_novels,'latest':latest_novels})