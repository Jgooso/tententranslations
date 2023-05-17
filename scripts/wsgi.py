from scripts.app import create_app
#from scripts.views import get_change_chapter_edit, get_change_chapter_upload, get_dates, get_descriptor_distribution, get_novels_page_count, novel_activation
from scripts.settings import ProdConfig,DevConfig
from flask import Flask, render_template
from flask_cors import CORS,cross_origin
from scripts.views import get_multiplenovels,get_singlenovel,get_chapter,get_genres_and_tags,get_schedules,get_noveltitles,get_user,get_home_page_novels,get_feedback,get_novels_page_count,get_dates,get_change_chapter_edit,get_descriptor_distribution,get_change_chapter_upload,uploadchapter,novel_activation
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
#@app.route('/test',methods=['GET','POST'])
#def test():
#    return testing()
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
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, DELETE, UPDATE, POST'
    return response
if __name__ == "__main__":
    app.run()

