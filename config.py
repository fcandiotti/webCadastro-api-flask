DEBUG = True

USERNAME = 'root'
PASSWORD = '102030Fernando'
SERVER = 'localhost'
DB = 'api_pontotel'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY="aplicacao_flask"