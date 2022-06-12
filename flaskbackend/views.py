import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import datetime
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
config = {
'user': 'root',
'password': 'zogjad-wucnaj-7tuRhi',
'host': '35.236.68.50',
'database': 'novels',
'raise_on_warnings': True,}
noveldb = mysql.connector.connect(**config)
novelcursor = noveldb.cursor(buffered=True)
genres = ['Action','Adult','Adventure','Comedy','Drame','Ecchi','Fantasy','Gender Bender','Harem',
'Historical','Horror','Josei','Martial Arts','Mature','Mecha','Mystery','Psychological','Romance',
'School Life','Sci-fi','Seinen','Shoujo','Shoujo Ai','Shounen Ai','Slice of Life','Smut',
'Sports','Supernatural','Tragedy','Wuxia','Xianxia','Xuanhuan','Yaoi','Yuri']
@app.route('/novels', methods = ['GET'])
def multiplenovels():
    tier= request.args.get('tier')
    novelsql = "SELECT * FROM novel"
    chaptersql = "SELECT chapternumber,date FROM Chapters WHERE CONTENT IS NOT NULL AND active <= %s AND novelid = %s ORDER BY chapternumber+0 DESC"
    novelObject = []
    novelcursor.execute(novelsql)
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
        except IndexError:
            try:
                novel['fristChapter'] = chapterResults[0]
            except IndexError:
                pass
    return jsonify(novelObject)
@app.route('/singlenovel', methods = ['GET'])
def singlenovel():
    novel = request.args.get('novel')
    tier = request.args.get('tier')
    novel_sql = "SELECT DISTINCT * FROM Novel WHERE novelid = %s"
    novel_val = (novel,)
    novelcursor.execute(novel_sql,novel_val)
    novel_results=novelcursor.fetchall()
    chapter_list = []
    novelData = []
    columnNames = [column[0] for column in novelcursor.description]
    for record in novel_results:
        novelData.append( dict( zip( columnNames , record ) ) )
    chapter_list_sql = "SELECT title,date,chapternumber,section,novelid,chapterorder FROM Chapters WHERE novelid = %s AND active <= %s ORDER BY chapterorder+0"
    chapter_list_val = (novel,tier)
    novelcursor.execute(chapter_list_sql,chapter_list_val)
    chapter_results = novelcursor.fetchall()
    chapter_column_names = [column[0] for column in novelcursor.description]
    chapter_list=[]
    for record in chapter_results:
        chapter_list.append( dict( zip( chapter_column_names , record ) ) )
    return jsonify({'Novel':novelData[0],'Chapters':chapter_list})

@app.route('/chapter', methods = ['GET'])
def get_chapter():
    chapter = request.args.get('chapter')
    novel = request.args.get('novel')
    chapter_sql = "SELECT DISTINCT content FROM Chapters WHERE chapternumber = %s AND novelid=%s;UPDATE Novel SET views = views +1 WHERE novelid = %s"
    chapter_val = (chapter,novel,novel)
    novelcursor.execute(chapter_sql,chapter_val,multi = True)
    for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
        if result.with_rows:
            chapter_results = novelcursor.fetchall()[0][0]
    noveldb.commit()
    return jsonify(chapter_results) 

@app.route('/uploaddata',methods=['Get'])
def get_genres_and_tags():
    return jsonify({'genres':genres})
app.run()
