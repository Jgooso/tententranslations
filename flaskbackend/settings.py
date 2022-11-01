import os

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_HEADER_PREFIX = 'Token'
    CORS_ORIGIN_WHITELIST = [
        'http://localhost:8080',
        'localhost:8080',
        'http://34.135.164.184'
    ],
    JWT_HEADER_TYPE = 'Token',
    #Access-Control-Allow-Origin: 'http://localhost:3000'

class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True