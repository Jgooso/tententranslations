import datetime
import os
#from jinja2 import Undefined
import mysql.connector
#import json
import pytz
#from PIL import Image
from scripts.scripts import download, processView, time_difference
from scripts.upload import manual_upload
from flask import jsonify, request, abort
import calendar
#import matplotlib.pylab as plt
from scripts.settings import DevConfig,ProdConfig
#Setup
config = DevConfig.SQL_SETTINGS
def get_multiplenovels():
    #Retrieve Data from Frontend
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    identifier = request.args.get('identifier').replace('|','&nbsp;')
    tier = request.args.get('tier')
    page = (int(request.args.get('page'))-1)*12
    order = request.args.get('order')
    if order == "views" or order == "length":
        order = order + ' DESC' 
    get_multiple_novel_val = (tier,identifier,tier,page)
    #multiple_novel_sql
    get_multiple_novel_chapter_sql =    """
                                        SELECT chapternumber,uploaddate 
                                        FROM chapters 
                                        WHERE CONTENT IS NOT NULL AND chapteractive >= %s AND novelid = %s 
                                        ORDER BY chapternumber+0 DESC LIMIT 2
                                    """
    if identifier != 'undefined':
        get_multiple_novel_sql = """ SELECT novels.novelid, novels.title, views.views as views,chapters.length,firstupload,lastupload
                                FROM novels 
                                    INNER JOIN noveldescriptors 
                                        ON novels.novelid = noveldescriptors.novelid 
                                    LEFT JOIN 
				                        (SELECT chapters.novelid,SUM(character_length(content)) as length FROM chapters WHERE chapteractive >= %s GROUP BY novelid) AS chapters
                                            ON chapters.novelid = novels.novelid
			                        LEFT JOIN (SELECT SUM(views) as views,novelid FROM view_data WHERE MONTH(date) = MONTH(CURDATE()) AND YEAR(date) = YEAR(CURDATE()) GROUP BY novelid) AS views
				                            ON novels.novelid = views.novelid
                                    INNER JOIN identifiers
                                        ON noveldescriptors.descriptor = identifiers.id
                                WHERE identifiers.descriptor = %s AND novels.novelactive >= %s
                                ORDER BY REPLACE("""+order+""",'"','')
                                LIMIT 12 OFFSET %s
                             """
        novelcursor.execute(get_multiple_novel_sql,get_multiple_novel_val)
    else:
        get_multiple_novel_sql = """
            SELECT novels.novelid, novels.title, views.views as views,chapters.length,firstupload,lastupload
		        FROM novels 
			        LEFT JOIN 
				        (SELECT chapters.novelid,SUM(character_length(content)) as length FROM chapters WHERE chapteractive >= %s GROUP BY novelid) AS chapters
                            ON chapters.novelid = novels.novelid
			        LEFT JOIN (SELECT SUM(views) as views,novelid FROM view_data WHERE MONTH(date) = MONTH(CURDATE()) AND YEAR(date) = YEAR(CURDATE()) GROUP BY novelid) AS views
				            ON novels.novelid = views.novelid
			    WHERE novels.novelactive >= %s
                ORDER BY """+order+"""
                LIMIT 12 OFFSET %s
             """
        novelcursor.execute(get_multiple_novel_sql,(tier,tier,page))
    novelData = novelcursor.fetchall()
    #Add chapters to novelData
    for novel in novelData:
        get_multiple_novel_val = (tier,novel['novelid'])
        novelcursor.execute(get_multiple_novel_chapter_sql,get_multiple_novel_val)
        chapterResults = novelcursor.fetchall()
        for chapter in chapterResults:
            chapter['uploaddate'] = time_difference(chapter['uploaddate'])
        try:
            novel['firstChapter'] = chapterResults[0]
            novel['secondChapter'] = chapterResults[1]
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
        
        get_single_novel_sql =  """SELECT DISTINCT novels.id,novels.novelid,novels.title,alternativetitle,description,url,novelactive, views.views as views
		                            FROM novels 
			                            LEFT JOIN (SELECT SUM(views) as views,novelid FROM view_data WHERE MONTH(date) = MONTH(CURDATE()) AND YEAR(date) = YEAR(CURDATE()) GROUP BY novelid) AS views
				                            ON novels.novelid = views.novelid
		                            WHERE novels.novelid = %s
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
                            SELECT title,novelid,uploaddate,chapternumber,section,chapterorder,chapteractive,chapteredited 
                                FROM chapters WHERE novelid = %s AND (chapteractive >= %s)
                                ORDER BY chapterorder+0
                           """
        get_chapter_list_val = (novel,tier)
        novelcursor.execute(get_single_novel_chapter_sql,get_chapter_list_val)
        chapter_list = novelcursor.fetchall()
       
        #Retrieve Novel identifiers
        get_single_novel_descriptor_sql = """SELECT identifiers.descriptor,identifiers.type 
                                FROM noveldescriptors 
                                    INNER JOIN identifiers 
                                        ON identifiers.id = noveldescriptors.descriptor 
                                WHERE noveldescriptors.novelid = %s"""
        get_single_novel_descriptor_val = (novel,)
        novelcursor.execute(get_single_novel_descriptor_sql,get_single_novel_descriptor_val)
        identifiers = novelcursor.fetchall()
        genres = []
        tags = []
        novelrelease = 0
        uploadstatus = 'nCompleted'
        novelstatus = 'uUnreleased'
        author = 'no author yet'
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
        if edit != 'True':
            for chapter in chapter_list:
                chapter['uploaddate'] = time_difference(chapter['uploaddate'])
        elif chapter_list[0]['uploaddate'] != None:
            for chapter in chapter_list:
                if chapter['uploaddate'] != None:
                    chapter['uploaddate'] = chapter['uploaddate'].isoformat(sep='T',timespec='auto')
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
        novelData = data['novelData']
        novelid = request.args.get('novel')
        post_single_novel_sql =  """
                                UPDATE novels SET description = %s, title = %s
                                    WHERE novelid = %s;
                                 """
        post_single_novel_val = (novelData['description'],novelData['title'],novelid)
        novelcursor.execute(post_single_novel_sql,post_single_novel_val)
        novelcursor.execute("DELETE FROM noveldescriptors WHERE novelid = %s",(novelid,))
        post_single_novel_descriptor_sql = "INSERT INTO noveldescriptors (novelid,descriptor) SELECT %s,id FROM identifiers WHERE descriptor = %s"
        for descriptor in data['genres'] + data['tags']+['n'+novelData['novelstatus'],novelData['novelrelease'],novelData['authors'],'u'+novelData['uploadstatus']]:
            post_single_novel_descriptor_val = (novelid,descriptor)
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
    if request.method == 'GET':
        get_chapter_sql = """
                       
                        SELECT DISTINCT title,content,chapteractive
                            FROM chapters 
                            WHERE novelid = %s and chapternumber = %s;
                      """
        chapter_val = (novel,chapter)
        chapter_results = []
        update_chapter_views_sql = " UPDATE view_data set views = views + (SELECT DISTINCT chapteractive FROM chapters WHERE novelid = %s AND chapternumber = %s) WHERE date = CURDATE() AND novelid = %s and chapternumber = %s;"
        update_chapter_views_val = (novel,chapter,novel,chapter)
        novelcursor.execute(get_chapter_sql,chapter_val)
        chapter_results = novelcursor.fetchone()
        novelcursor.execute(update_chapter_views_sql,update_chapter_views_val)
        print('working')
        noveldb.commit()
        noveldb.close()
        return jsonify(chapter_results)
    if request.method == 'PUT':
        data = request.get_json()
        put_chapter_sql = 'UPDATE chapters SET content = %s, title = %s WHERE novelid = %s and chapternumber = %s'
        put_chapter_val = (data['content'],data['title'],novel,chapter)
        novelcursor.execute(put_chapter_sql,put_chapter_val)
        noveldb.commit()
        noveldb.close()
        return chapter

def get_genres_and_tags():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        novelcursor.execute('SELECT * FROM identifiers WHERE type = "tag" OR type = "genre" ORDER BY descriptor')
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
    if request.method == 'POST':
        local = pytz.timezone("America/Chicago")
        data = request.form
        novel = data['novel']
        date = [int(d) for d in data['upload-start'].split('-')]
        start_date = datetime.datetime(date[0],date[1],date[2])
        times = [datetime.time(int(data[t][:2])) for t in data if 'time' in t]
        days_of_the_week = [int(data[w]) for w in data if 'day' in w]
        dates = []
        novelcursor.execute('SELECT COUNT(content) as length FROM chapters WHERE novelid = %s',(novel,))
        length = novelcursor.fetchone()['length']
        i = 0
        while len(dates) < length:
            day = start_date + datetime.timedelta(days=i)
            if (day.weekday()+1)%7 in days_of_the_week:
                for t in times:
                    dates.append(datetime.datetime.combine(day,t).astimezone(local))
                    if len(dates) >= length:
                        break

            if(i > 100):
                break
            i+=1
        for d in dates:
            d = d.astimezone(pytz.UTC)
            date_sql = """
                SET @a = (SELECT DISTINCT content IS NULL FROM chapters WHERE novelid = %s and uploaddate IS NULL LIMIT 1)+1;
                PREPARE STMT FROM "UPDATE chapters SET uploaddate = %s
	                WHERE novelid = %s and uploaddate IS NULL 
	                ORDER BY chapterorder 
	                LIMIT ?;";
                    EXECUTE STMT USING @a; 
            """
            date_val = (novel,d,novel)
            for result in novelcursor.execute(date_sql,date_val,multi=True):
                continue
        noveldb.commit()
        noveldb.close()
        return data

def get_noveltitles():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        novelcursor.execute("""
                                SELECT title,novels.novelid,completed_percentage FROM novels INNER JOIN
                                    (SELECT novelid,SUM(chapteredited)/COUNT(novelid) as completed_percentage
                                        FROM  chapters
                                        GROUP BY novelid) AS chapters 
                                    ON novels.novelid = chapters.novelid
                                    ORDER BY completed_percentage DESC, title
                                    
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
        noveldb.close()
        return jsonify(user)
    if request.method == 'POST':
        data = request.get_json()
        user_id = data['userID']
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
                                        WHERE CONTENT IS NOT NULL AND chapteractive >= %s AND novelid = %s 
                                        ORDER BY chapternumber+0 DESC LIMIT 2
                                    """
        home_page_popular_sql = """
                                SELECT novels.novelid,novels.title,novelactive,description,sum(chapters.views) as views,ROW_NUMBER() OVER (ORDER BY sum(chapters.views) DESC) row_num,ANY_VALUE(genre.des) as genre
                                FROM novels LEFT JOIN (SELECT view_data.views,chapters.novelid,content FROM chapters 
							                            LEFT JOIN view_data ON view_data.chapternumber = chapters.chapternumber and view_data.novelid = chapters.novelid WHERE MONTH(date) = MONTH(CURDATE()) AND YEAR(date) = YEAR(CURDATE())) AS chapters ON chapters.novelid = novels.novelid
                                LEFT JOIN (
                                        SELECT identifiers.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN identifiers ON noveldescriptors.descriptor = identifiers.id
                                            WHERE type = 'genre'
                                            ORDER BY identifiers.descriptor
                                    ) AS genre
                                        ON genre.nov = novels.novelid
                                    WHERE novelactive >= %s
                                    GROUP BY novels.id
                                    ORDER BY views DESC
                                    LIMIT 9;
                            """
        home_page_recent_sql =  """
                                SELECT title,novels.novelid,ANY_VALUE(genre.des) AS genre,novelactive FROM novels 
                                    LEFT JOIN (
                                        SELECT identifiers.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN identifiers ON noveldescriptors.descriptor = identifiers.id
                                            WHERE type = 'genre'
                                            ORDER BY identifiers.descriptor
                                    ) AS genre
                                        ON genre.nov = novels.novelid
                                    WHERE novelactive >= %s
	                                GROUP BY novels.id
                                    ORDER BY firstupload
                                    LIMIT 7;
                            """
        home_page_latest_sql =  """
                                SELECT title,novels.novelid,ANY_VALUE(genre.des) AS genre,novelactive FROM novels 
                                    LEFT JOIN (
                                        SELECT identifiers.descriptor AS des ,noveldescriptors.novelid AS nov
                                            FROM noveldescriptors INNER JOIN identifiers ON noveldescriptors.descriptor = identifiers.id
                                            WHERE type = 'genre'
                                            ORDER BY identifiers.descriptor
                                    ) AS genre
                                        ON genre.nov = novels.novelid
                                    WHERE novelactive >= %s
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
            get_multiple_novel_val = (tier,novel['novelid'])
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
        noveldb.commit()
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
                                        ON novels.novelid = noveldescriptors.novelid 
                                    INNER JOIN identifiers
                                        ON noveldescriptors.descriptor = identifiers.id
                                    WHERE novelactive >= %s AND 
                                        identifiers.descriptor = %s
                                        
                                """,(tier,identifier))
        else:
             novelcursor.execute("SELECT COUNT(novelid) as count FROM novels WHERE novelactive >= %s",(tier,) )
        novel_count = (int(novelcursor.fetchone()['count']))
        page_count = ((novel_count)//12)+1
        noveldb.close()
        return {'page_count':page_count,'novel_count':novel_count}

#ADD REMAINING FILE SIZE

def get_dates():
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True,dictionary=True)
    if request.method == 'GET':
        offset= int(request.args.get('offset'))
        month = int(request.args.get('month'))
        year = int(request.args.get('year'))
        month_name = datetime.datetime.strptime(str(month), "%m").strftime("%B")
        end_day = calendar.monthrange(year, month)[1]
        start_date = datetime.date(year, month, 1) 
        end_date = datetime.date(year, month, end_day) 
        delta = end_date - start_date   # returns timedelta
        calender = {'month':month_name,'weekday_start':(start_date.weekday()+1)%7,'days':{}}
        get_schedule__sql = ('SELECT novels.title,uploaddate FROM chapters INNER JOIN novels ON novels.novelid = chapters.novelid WHERE uploaddate BETWEEN %s AND %s')
        get_schedule_val = (start_date,end_date)
        novelcursor.execute(get_schedule__sql,get_schedule_val)
        schedule_list = novelcursor.fetchall()
        schedule_bucket = {}
        for schedule in schedule_list:
            day = schedule['uploaddate'] - datetime.timedelta(minutes=offset)
            if day.day not in schedule_bucket:
                schedule_bucket[day.day] = []
            schedule_bucket[day.day].append({'novel':schedule['title'],'hour':day.hour})
        for i in range(delta.days + 1):
            day = start_date + datetime.timedelta(days=i)
            calender['days'][day.day] = []
            try:
                for d in schedule_bucket[day.day]:
                    calender['days'][day.day].append(d)
            except:
                pass
        noveldb.close()
        return jsonify(calender)
def testing():
    if request.method=='POST':
        file_name = request.files['file'].filename
        file = convertToBinaryData(request.files['file'])
       
        with open(os.path.join('./static/assets',file_name),'wb') as f:
            f.write(file)
        return request.method
def get_database_size():
    if request.method == 'GET':
       pass
def uploadchapter():
    if request.method == 'POST':
        novel = request.args.get('novel')
        manual_upload(novel)
        return 'posted'
def get_change_chapter_edit():
    if request.method == 'PUT':
        noveldb = mysql.connector.connect(**config)
        novelcursor = noveldb.cursor(buffered=True,dictionary=True)
        edit = request.args.get('edit')
        novel = request.args.get('novel')
        chapter = request.args.get('chapter')
        novelcursor.execute("UPDATE chapters SET chapteredited = %s WHERE novelid = %s and chapterorder = %s",(edit,novel,chapter))
        noveldb.commit()
        noveldb.close()
        return chapter
def get_change_chapter_upload():
    if request.method == 'PUT':
        noveldb = mysql.connector.connect(**config)
        novelcursor = noveldb.cursor(buffered=True,dictionary=True)
        novel = request.args.get('novel')
        chapter = request.args.get('chapter')
        offset = request.args.get('offset')
        date = request.get_json()['date'] + offset
        novelcursor.execute('UPDATE chapters SET uploaddate = %s WHERE novelid = %s and chapterorder = %s',(date,novel,chapter))
        noveldb.commit()
        noveldb.close()
        return novel
def convertToBinaryData(file):
    # Convert digital data to binary format
    binaryData = file.read()
    return binaryData
def get_descriptor_distribution():
    if request.method == 'GET':
        noveldb = mysql.connector.connect(**config)
        novelcursor = noveldb.cursor(buffered=True,dictionary=True)
        novelcursor.execute('SELECT identifiers.descriptor, T.count,type FROM identifiers INNER JOIN (SELECT descriptor,COUNT(descriptor) as count FROM noveldescriptors GROUP BY descriptor) AS T ON T.descriptor = identifiers.id')
        descriptor_list = novelcursor.fetchall()
        descriptor_bucket = {}
        for d in descriptor_list:
            if d['type'] not in descriptor_bucket:
                descriptor_bucket[d['type']] = []
            descriptor_bucket[d['type']].append(d)
        return jsonify(descriptor_bucket)
def get_novel_analytics():
    if request.method == 'GET':
        start_date = request.args.get('start')
        end_date = request.args.get('end')
        novel = request.args.get('novel')
def novel_activation():
    if request.method == 'PUT':
        novelactive = request.args.get('active')
        novel = request.args.get('novel')
        noveldb = mysql.connector.connect(**config)
        novelcursor = noveldb.cursor(buffered=True)
        novelcursor.execute("UPDATE novels SET novelactive = %s WHERE novelid = %s",(novelactive,novel))
        novelcursor.execute("UPDATE noveldescriptors SET descriptor = " )
        noveldb.commit()
        noveldb.close()
        return 'put'
def uploadchapter():
    if request.method == 'PUT':
        novel = request.args.get('novel')
        manual_upload(novel)
        return novel
def put_resetschedule():
    if request.method == 'PUT':
        novel = request.args.get('novel')
        noveldb = mysql.connector.connect(**config)
        novelcursor = noveldb.cursor(buffered=True)
        novelcursor.execute("UPDATE chapters SET uploaddate = NULL WHERE novelid = %s",(novel,))
        noveldb.commit()
        noveldb.close()
        return novel