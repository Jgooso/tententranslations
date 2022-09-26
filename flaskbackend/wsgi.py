from app import create_app
from settings import ProdConfig
from flask_cors import CORS,cross_origin
from views import *
import stripe

app = create_app(ProdConfig)
'''
stripe_keys = {
    "secret_key": os.environ["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"],
    "publishable_key": os.environ["pk_live_51L5d0fHlYhKzvWmvp72z9v2OaWS2tVyk9w4LPvRTs2H5s3txY36Y5DoChXe0aAYwAmUqCWFtHqZEE0chlURjOAgl00fZShWX43"],
    }
stripe.api_key = stripe_keys["secret_key"]
'''
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
@app.route('/schedule',methods=['GET','POST','PUT','DELETE'])
def schedules():
    return get_schedules()
@app.route('/noveltitles',methods=['GET'])
def noveltitles():
    return get_noveltitles()
@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, DELETE, UPDATE, POST'
    return response
@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)
if __name__ == "__main__":
    app.run()