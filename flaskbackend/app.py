from flask import Flask
from flask_cors import CORS
from settings import ProdConfig, DevConfig
from scripts import download




def create_app(config_objct=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_objct)
    CORS(app, resources={r'*':{'origins':['localhost:5000']}})
    
    return app


