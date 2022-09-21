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
    category = request.args.get('category')[6:]
    identifier = request.args.get('identifier').strip()
    tier= request.args.get('tier')
    print(category,identifier,tier)
    novelsql = 'SELECT * FROM novels'
    novelcursor.execute(novelsql)
    chaptersql = "SELECT chapternumber,uploaddate FROM chapters WHERE CONTENT IS NOT NULL AND chapteractive <= %s AND novelid = %s ORDER BY chapternumber+0 DESC"
    novelObject = []
    novelresults = novelcursor.fetchall()
    columnNames = [column[0] for column in novelcursor.description]
    for record in novelresults:
        novelObject.append( dict( zip( columnNames , record ) ) )
    for novel in novelObject:
        val = (tier,novel['novelid'])
        novelcursor.execute(chaptersql,val)
        chapterResults = novelcursor.fetchall()
        try:
            novel['firstChapter'] = chapterResults[0]
            novel['secondChapter']=chapterResults[1]
            novel['tags'] = novel['tags'].split(',')
            novel['genres'] = novel['genres'].split(',')
        except IndexError:
            try:
                novel['fristChapter'] = chapterResults[0]
            except IndexError:
                pass
    if category == 'tags' or category == 'genres':
        novelObject = [novel for novel in novelObject if identifier in novel[category]]
        print(novel[category])
    elif category == 'ned':
        print('browse')
        return jsonify(novelObject)
    else:
        novelObject = [novel for novel in novelObject if novel[category] == identifier]
    return jsonify(novelObject)

def singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    if request.method == 'GET':
        novel_sql = "SELECT DISTINCT * FROM novels WHERE novelid = %s"
        novel_val = (novel,)
        novelcursor.execute(novel_sql,novel_val)
        novel_results=novelcursor.fetchall()
        chapter_list = []
        columnNames = [column[0] for column in novelcursor.description]
        for record in novel_results:
            novelData =  dict( zip( columnNames , record ) ) 
        novelData['tags'] = novelData['tags'].split(',')
        novelData['genres'] = novelData['genres'].split(',')
        chapter_list_sql = "SELECT title,uploaddate,chapternumber,section,novelid,chapterorder FROM chapters WHERE novelid = %s AND chapteractive <= %s ORDER BY chapterorder+0"
        chapter_list_val = (novel,tier)
        novelcursor.execute(chapter_list_sql,chapter_list_val)
        chapter_results = novelcursor.fetchall()
        chapter_column_names = [column[0] for column in novelcursor.description]
        chapter_list=[]
        for record in chapter_results:
            chapter_list.append( dict( zip( chapter_column_names , record ) ) )
        novelData['views'] = processView(novelData['views'])
        return jsonify({'Novel':novelData,'Chapters':chapter_list})
    if request.method == 'POST':
        data = request.get_json()
        input_tags = ','.join(data['tags'])
        input_genres = data['genres']
        input_url = data['url']
        print(input_url)
        download(URL=input_url,tags=input_tags,genres=input_genres)
        return data
    if request.method == 'PUT':
        data = request.get_json()
        sql = 'UPDATE novels SET description = %s, genres = %s, tags = %s, novelstatus = %s WHERE novelid = %s'
        val = (data['description'],','.join(data['genres']),','.join(data['tags']),data['completed'],novel)
        novelcursor.execute(sql,val)
        noveldb.commit()
        return data
    if request.method == 'DELETE':
        sql = 'DELETE FROM novels WHERE novelid=%s'
        val = (novel,)
        novelcursor.execute(sql,val)
        noveldb.commit()
def get_chapter():
    chapter = request.args.get('chapter')
    novel = request.args.get('novel')
    if request.method == 'GET':
        chapter_sql = "SELECT DISTINCT content FROM chapters WHERE chapternumber = %s AND novelid=%s;UPDATE novels SET views = views +1 WHERE novelid = %s"
        chapter_val = (chapter,novel,novel)
        novelcursor.execute(chapter_sql,chapter_val,multi = True)
        for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
            if result.with_rows:
                chapter_results = novelcursor.fetchall()[0][0]
        noveldb.commit()
        return jsonify(chapter_results) 
    if request.method == 'PUT':
        data = request.get_json()
        sql = 'UPDATE chapters SET content = %s WHERE chapternumber = %s AND novelid = %s'
        val = (data['content'],chapter,novel)
        novelcursor.execute(sql,val)
        print(data)
        return data
def get_genres_and_tags():
    if request.method == 'GET':
        novelcursor.execute('SELECT * FROM noveldescriptors')
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
        novelcursor.execute('SELECT schedule.*,novels.title FROM schedule INNER JOIN novels ON novels.novelid=schedule.novel')
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
            schedule_creator_sql = 'INSERT INTO schedule (novel,time,day) SELECT novelid, %s,%s FROM novels WHERE title = %s'
            schedule_creator_val = (input_time,date,input_novel)
            novelcursor.execute(schedule_creator_sql,schedule_creator_val)
            print(date)
        noveldb.commit()
        return data

def get_noveltitles():
    if request.method == 'GET':
        novelcursor.execute('SELECT title,novelid FROM novels')
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

