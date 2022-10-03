import datetime
from operator import indexOf
import mysql.connector
import json
from scripts import download, processView, ranker
from flask import Flask, jsonify, request, session
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

def multiplenovels():
    #Retrieve Data from Frontend
    try:
        category = request.args.get('category')[request.args.get('category').index('-')+1:]
    except ValueError:
        category = request.args.get('category')
    identifier = request.args.get('identifier').replace('-','&nbsp;')
    tier= request.args.get('tier')
    multiple_novel_val = (identifier,)
    #multiple_novel_sql
    if category == 'tags' or category == 'genres' or category == 'status':
        multiple_novel_sql = 'SELECT novels.novelid,title,views,rating,lastupload,firstupload,imageurl FROM novels INNER JOIN noveldescriptors ON novels.novelid = noveldescriptors.novelid WHERE descriptor = %s'
    elif category == 'authors':
        multiple_novel_sql = 'SELECT novelid,title,views,rating,lastupload,firstupload,imageurl FROM novels WHERE authors = %s'
    else:
        multiple_novel_sql = 'SELECT novelid,title,views,rating,lastupload,firstupload,imageurl FROM novels'
    
    multiple_novel_chapter_sql = "SELECT chapternumber,uploaddate FROM chapters WHERE CONTENT IS NOT NULL AND chapteractive <= %s AND novelid = %s ORDER BY chapternumber+0 DESC LIMIT 2"
    if category=='undefined':
         novelcursor.execute(multiple_novel_sql)
    else:
        novelcursor.execute(multiple_novel_sql,multiple_novel_val)

    novelObject = []
    novelresults = novelcursor.fetchall()
    columnNames = [column[0] for column in novelcursor.description]
    for record in novelresults:
        novelObject.append( dict( zip( columnNames , record ) ) )
    
    for novel in novelObject:
        val = (tier,novel['novelid'])
        novelcursor.execute(multiple_novel_chapter_sql,val)
        chapterResults = novelcursor.fetchall()
        novel['firstChapter'] = chapterResults[0]
        try:
            novel['secondChapter']=chapterResults[1]
        except IndexError:
           pass
    return jsonify(novelObject)

def singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    edit = request.args.get('edit')
    if request.method == 'GET':
        #Retrieve Novel Data
        novel_sql = "SELECT DISTINCT * FROM novels WHERE novelid = %s"
        novel_val = (novel,)
        novelcursor.execute(novel_sql,novel_val)
        novel_results=novelcursor.fetchall()
        columnNames = [column[0] for column in novelcursor.description]
        for record in novel_results:
            novelData =  dict( zip( columnNames , record ) ) 
        novelData['views'] = processView(novelData['views'])

        #Retrieve Chapters
        chapter_list_sql = "SELECT title,uploaddate,chapternumber,section,novelid,chapterorder FROM chapters WHERE novelid = %s AND chapteractive <= %s ORDER BY chapterorder+0"
        chapter_list_val = (novel,tier)
        novelcursor.execute(chapter_list_sql,chapter_list_val)
        chapter_results = novelcursor.fetchall()
        chapter_column_names = [column[0] for column in novelcursor.description]
        chapter_list=[]
        for record in chapter_results:
            chapter_list.append( dict( zip( chapter_column_names , record ) ) )
       
        #Retrieve Novel Descriptors
        descriptor_sql = "SELECT noveldescriptors.descriptor,descriptors.type FROM noveldescriptors INNER JOIN descriptors ON descriptors.descriptor = noveldescriptors.descriptor WHERE noveldescriptors.novelid = %s"
        novelcursor.execute(descriptor_sql,novel_val)
        descriptors = novelcursor.fetchall()
        genres = []
        tags = []
        for descriptor in descriptors:
            if descriptor[1] == 'genre':
                genres.append(descriptor[0])
            elif descriptor[1] == 'tag':
                tags.append(descriptor[0])
            elif descriptor[1] == 'uploadstatus':
                status = descriptor[0]
        novelData['tags'] = tags
        novelData['genres'] = genres
        novelData['uploadstatus'] = status
        #Editable get Genres and tags
        if(edit=='True'):
            novelcursor.execute('SELECT * FROM descriptors WHERE type = "tag" OR type = "genre"')
            descriptors = novelcursor.fetchall()
            genres = []
            tags = []
            for descriptor in descriptors:
                if descriptor[1] == 'tag':
                    tags.append(descriptor[0])
                elif descriptor[1] == 'genre':
                    genres.append(descriptor[0])
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
        novel_update_sql = 'UPDATE novels SET description = %s, novelstatus = %s, title = %s WHERE novelid = %s;DELETE FROM noveldescriptors WHERE novelid = %s; '
        novel_update_val = (data['description'],data['completed'],data['title'],novel,novel)
        results = novelcursor.execute(novel_update_sql,novel_update_val,multi=True)
        for cur in results:
            print(cur)
        descriptor_update_sql = 'INSERT INTO noveldescriptors (novelid, descriptor)VALUES (%s,%s)'
        for descriptor in data['genres'] + data['tags']+['Ongoing']:
            descriptor_update_val = (novel,descriptor)
            novelcursor.execute(descriptor_update_sql,descriptor_update_val)

        noveldb.commit()
        return data
    if request.method == 'DELETE':#Delete Novel
        sql = 'DELETE FROM novels WHERE novelid=%s'
        val = (novel,)
        novelcursor.execute(sql,val)
        noveldb.commit()

def get_chapter():
    chapter = request.args.get('chapter')
    novel = request.args.get('novel')
    update_chapter = request.args.get('chapterupdate')
    if request.method == 'GET':
        chapter_sql = "SELECT DISTINCT content FROM chapters WHERE chapternumber = %s AND novelid=%s;UPDATE novels SET views = views +1 WHERE novelid = %s"
        chapter_val = (chapter,novel,novel)
        chapter_results = []
        for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
            if result.with_rows:
                chapter_results = novelcursor.fetchall()[0][0]
        noveldb.commit()
        return jsonify(chapter_results) 
    if request.method == 'PUT':
        data = request.get_json()
        try:
            sql = 'UPDATE chapters SET content = %s WHERE chapternumber = %s AND novelid = %s'
            val = (data['content'],update_chapter,novel)
            novelcursor.execute(sql,val)
        except:
            print(update_chapter,novel)
            
        chapter_sql = "SELECT DISTINCT content FROM chapters WHERE chapternumber = %s AND novelid=%s"
        chapter_val = (chapter,novel)
        novelcursor.execute(chapter_sql,chapter_val)
        chapter_data = novelcursor.fetchone()
        return jsonify(chapter_data)

def get_genres_and_tags():
    if request.method == 'GET':
        novelcursor.execute('SELECT * FROM descriptors WHERE type = "tag" OR type = "genre"')
        descriptors = novelcursor.fetchall()
        genres = []
        tags = []
        for descriptor in descriptors:
            if descriptor[1] == 'tag':
                tags.append(descriptor[0])
            elif descriptor[1] == 'genre':
                genres.append(descriptor[0])
        return jsonify({'genres':genres, 'tags':tags})
    
def get_schedules():
    if request.method == 'GET':
        novel = request.args.get('novel')
        schedule_select_sql = ('SELECT * FROM schedule WHERE novelid = %s')
        schedule_select_val = (novel,)
        novelcursor.execute(schedule_select_sql,schedule_select_val)
        schedules = novelcursor.fetchall()
        chapter_column_names = [column[0] for column in novelcursor.description]
        schedule_list=[]
        for record in schedules:
            schedule_list.append( dict( zip( chapter_column_names , record ) ) )
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
            schedule_creator_sql = 'INSERT INTO schedule (novelid,time,day) VALUES (%s,%s,%s)'
            schedule_creator_val = (input_novel,input_time,date)
            novelcursor.execute(schedule_creator_sql,schedule_creator_val)
            print(date)
        noveldb.commit()
        return data

def get_noveltitles():
    if request.method == 'GET':
        novelcursor.execute('SELECT title,novels.novelid FROM novels INNER JOIN noveldescriptors ON novels.novelid = noveldescriptors.novelid WHERE descriptor in ("Ongoing","On Hold","Dropped")')
        novels = novelcursor.fetchall()
        chapter_column_names = [column[0] for column in novelcursor.description]
        novel_list=[]
        for record in novels:
            novel_list.append( dict( zip( chapter_column_names , record ) ) )
        return jsonify(novel_list)
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        novelcursor.execute('SELECT * FROM users WHERE username = %s AND password = %s',(username,password))
        account = novelcursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

