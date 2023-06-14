from flask import Flask
from flask_cors import CORS
from scripts.settings import ProdConfig, DevConfig



def create_app(config_objct=DevConfig):
    app = Flask(__name__,
            static_folder = "../static",
            template_folder = "../template")
    app.config.from_object(config_objct)
    CORS(app, resources={r'*':{'origins':['*']}})
    
    return app
