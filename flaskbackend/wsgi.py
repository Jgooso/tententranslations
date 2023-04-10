from app import create_app
from settings import ProdConfig
from flask import Flask
from flask_cors import CORS,cross_origin
from views import *
app = create_app(ProdConfig)

@app.route('/novel/multiple', methods = ['GET'])
def multiplenovels():
    return get_multiplenovels()
@app.route('/novel/single', methods = ['GET','POST','PUT','DELETE'])
def singlenovel():
    return get_singlenovel()
@app.route('/chapter', methods = ['GET','PUT'])
def chapter():
    return get_chapter()
@app.route('/uploaddata',methods=['GET'])
def genres_and_tags():
    return get_genres_and_tags()
@app.route('/schedule',methods=['GET','POST','PUT','DELETE'])
def schedules():
    return get_schedules()
@app.route('/noveltitles',methods=['GET'])
def noveltitles():
    return get_noveltitles()
@app.route('/user',methods=['GET','POST'])
def user():
    return get_user()
@app.route('/home',methods=['GET'])
def home():
    return get_home_page_novels()
@app.route('/feedback',methods=['GET','POST','DELETE'])
def feedback():
    return get_feedback()
@app.route('/novels-page-count',methods=['GET'])
def novel_page_count():
    return get_novels_page_count()
@app.route('/dates',methods=['GET'])
def dates():
    return get_dates()
@app.route('/chaptereditchange',methods=['PUT'])
def change_chapter_edit():
    return get_change_chapter_edit()
@app.route('/test',methods=['GET','POST'])
def test():
    return testing()
@app.route('/descriptorbution',methods=['GET'])
def descriptor_distribution():
    return get_descriptor_distribution()
@app.route('/uploadchapter',methods=['GET'])
def upload_chapter():
    return upload()
@app.route('/chapteruploadchange',methods = ['PUT'])
def change_chapter_upload():
    return get_change_chapter_upload()
@app.route('/uploadchapter',methods = ['PUT'])
def upload():
    return uploadchapter()
@app.route('/activatenovel',methods = ['PUT'])
def activatenovel():
    return novel_activation()
@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, DELETE, UPDATE, POST'
    return response
if __name__ == "__main__":
    app.run()