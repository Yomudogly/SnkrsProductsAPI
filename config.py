import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS= { 'db' : os.environ.get('DB_NAME'),
                       'host' :  os.environ.get('DB_CONNECTION_STRING')}
    JWT_SECRET_KEY = os.environ.get('ANOTHER_SECRET_KEY')
    DEBUG = True          # some Flask specific configs
    CACHE_TYPE = 'simple' # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 300