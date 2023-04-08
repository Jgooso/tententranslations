from flask import Flask
from flask_cors import CORS
from settings import ProdConfig, DevConfig




def create_app(config_objct=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_objct)
    CORS(app, resources={r'*':{'origins':['*']}})
    
    return app


