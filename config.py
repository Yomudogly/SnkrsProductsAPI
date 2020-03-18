import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS= { 'db' : os.environ.get('DB_NAME'),
                       'host' :  os.environ.get('DB_CONNECTION_STRING')}
    JWT_SECRET_KEY = os.environ.get('ANOTHER_SECRET_KEY')