from app import create_app
from settings import ProdConfig
from flask_cors import CORS,cross_origin
from views import *

app = create_app(ProdConfig)

@app.route('/novel/multiple', methods = ['GET'])
@cross_origin()
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
@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, DELETE, UPDATE, POST'
    return response
if __name__ == "__main__":
    app.run()