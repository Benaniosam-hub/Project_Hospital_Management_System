import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY','')
    DEBUG = os.environ.get('FLASK_DEBUG', True)

    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME','hospital_db')
    DB_USER = os.environ.get('DB_USER','postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_PORT = os.environ.get('DB_PORT','5432')

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY','')
    JWT_ACCESS_TOKEN_EXPIRES = 3600 # 3600seconds expire time
