import datetime
import os
from jinja2 import Undefined
import mysql.connector
#import json
import pytz
from PIL import Image
from flask import Flask, jsonify, request, session
config = {
'user': 'root',
'password': 'jeg4Iphone',
'host': '127.0.0.1',
'port': '3306',
'database': 'tententranslations',
'raise_on_warnings': True,}
def get_feedback():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        page= int(request.args.get('page'))
        novelcursor.execute("SELECT * FROM feedback LIMIT 5 OFFSET %s",(page,))
        feedback_list = novelcursor.fetchall()
        return jsonify(feedback_list)
    if request.method == 'POST':
        feedback = request.get_json()['feedback']
        novelcursor.execute("INSERT INTO feedback(feedback) VALUES (%s)",(feedback,))
        noveldb.commit()
        return 'posted'
    if request.method == 'DELETE':
        id= request.args.get('id')
        novelcursor.execute("DELETE FROM feedback WHERE id = %s",(id,))
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