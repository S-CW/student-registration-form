import os
from dotenv import load_dotenv

load_dotenv()

# Add configuration to factory application.
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')

# Athentication setting
LOGIN_DISABLED = os,os.environ.get('LOGIN_DISABLED')