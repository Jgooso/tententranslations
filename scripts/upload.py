import mysql.connector
from scripts.settings import DevConfig,ProdConfig
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
config = ProdConfig.SQL_SETTINGS
def schedule_upload():#change permissions for viewing of novels
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True)
    chapter_sql =  """
                   UPDATE chapters SET chapteractive = 1 WHERE DATE(uploaddate) = CURDATE() AND HOUR(uploaddate) = HOUR(NOW());
                   UPDATE novels INNER JOIN chapters on novels.novelid = chapters.novelid SET lastupload = NOW(),novelactive = 1 WHERE DATE(uploaddate) = CURDATE() AND HOUR(uploaddate) = HOUR(NOW());
                   SELECT novelid,section FROM chapters WHERE DATE(uploaddate) = CURDATE() AND HOUR(uploaddate) = HOUR(NOW())
                   """
    for result in novelcursor.execute(chapter_sql,multi=True):
            if result.with_rows:
                chapter_val = novelcursor.fetchall()
    print(chapter_val)
    for ch in chapter_val:
        novelcursor.execute("UPDATE chapters SET chapteractive = 1 WHERE novelid = %s AND section = %s AND chapternumber = 0",ch)
     #upload_bot(novelcursor=novelcursor,novel)
    noveldb.commit()
    noveldb.close()
def manual_upload(novel):
    noveldb = mysql.connector.connect(**config)
    novelcursor = noveldb.cursor(buffered=True)
    get_chapter_sql = "SELECT chapternumber FROM chapters WHERE novelid = %s and chapteractive = 0"
    get_chapter_val = (novel,)
    novelcursor.execute(get_chapter_sql,get_chapter_val)
    if(novelcursor.fetchone()[0] == 0):
        limit = 2
    else:
        limit = 1
    chapter_sql ="""
            UPDATE chapters SET chapteractive = 1 WHERE novelid = %s AND chapteractive = 0 LIMIT %s;
            UPDATE novels SET lastupload = NOW(),novelactive = 1 WHERE novelid = %s;
            """
    chapter_val = (novel,limit,novel)
    for result in novelcursor.execute(chapter_sql,chapter_val,multi=True):
        continue
    noveldb.commit()
    noveldb.close()
def upload_bot(novelcursor,novel):
    novelcursor.execute("SELECT novels.title,novels.novelid,chapters.chapternumber FROM chapters INNER JOIN novels ON chapters.novelid = novels.id WHERE chapteractive = 1 and novels.id = %s ORDER BY chapternumber+0 DESC LIMIT 1",(novel,))
    chapter = novelcursor.fetchone()
    novel_title = chapter[0]
    link = 'https://tententranslation/novels/'+str(chapter[1])+'/'+str(chapter[2])
    #print(link)
    #print(novel_title)
    chapter_number = chapter[2]
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://www.novelupdates.com')
    #GET TO LOGIN PAGE
    browser.find_element(by=By.LINK_TEXT, value='Login').click()
    browser.find_element(by=By.ID, value='user_login').send_keys("jgooso")
    browser.find_element(by=By.ID, value = 'user_pass').send_keys("testingpassword")
    browser.find_element(by=By.ID, value = 'wp-submit').click()
    #GET TO UPLOAD PAGE
    browser.find_elements(by=By.ID, value='menu_right_item')[1].click()
    browser.find_element(by=By.LINK_TEXT, value='User Profile').click()
    browser.find_element(by=By.CLASS_NAME,value = 'ptool').click()
    #TYPE DATA INTO BOXES
    browser.find_element(by=By.ID, value = 'title_change_100').send_keys(novel_title)
    browser.find_element(by=By.ID, value = 'arrelease').send_keys(chapter_number)
    browser.find_element(by=By.ID,value = 'arlink').send_keys(link)
    browser.find_element(by=By.ID,value='group_change_100').send_keys('tententranslations')
    #SUBMIT

    #CLOSE BOT
    browser.close()