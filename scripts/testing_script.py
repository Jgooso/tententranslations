#import mysql.connector
#downloading novels and chapters
#import string, random
#import re, requests
#import language_tool_python
#from bs4 import BeautifulSoup
#from googletrans import Translator
#from settings import Config
#from datetime import datetime,date,timedelta
#config = Config.SQL_SETTINGS
#noveldb = mysql.connector.connect(**config)
#novelcursor = noveldb.cursor(buffered=True)
#novelcursor.execute("SELECT novelid,chapternumber FROM chapters WHERE chapternumber != 0")
#chapters = novelcursor.fetchall()
#def daterange(start_date, end_date):
#    for n in range(int((end_date - start_date).days)):
#        yield start_date + timedelta(n)
#for chapter in chapters:
#    start_date = date(2023, 4, 10)
#    end_date = date(2026, 12, 31)
#    print(chapter)
#    for single_date in daterange(start_date, end_date):
#        chapter_val = (chapter[0],chapter[1],single_date)
#        novelcursor.execute("INSERT INTO view_data(novelid,chapternumber,date) VALUES (%s,%s,%s)",chapter_val)
#noveldb.commit()
#noveldb.close()

