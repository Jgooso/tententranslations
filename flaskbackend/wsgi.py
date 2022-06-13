from app import create_app
from settings import ProdConfig
from flask_cors import CORS,cross_origin
from views import multiplenovels,singlenovel,get_chapter,get_genres_and_tags
app = create_app(ProdConfig)
@app.route('/novel/multiple', methods = ['GET'])
@cross_origin()
def multinovel():
    return multiplenovels()
@app.route('/novel/single', methods = ['GET','POST','PUT','DELETE'])
def onenovel():
    return singlenovel()
@app.route('/chapter', methods = ['GET','PUT'])
def chapter():
    return get_chapter()
@app.route('/uploaddata',methods=['GET'])
def upload():
    return get_genres_and_tags()
@app.after_request
def add_header(response):
    response.access_control_allow_origin = "*"
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    return response
app.run()