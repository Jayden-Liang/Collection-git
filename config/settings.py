import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path=env_path)

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                                            'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
                                                                        'Collection/app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv('SECRET_KEY')



MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

