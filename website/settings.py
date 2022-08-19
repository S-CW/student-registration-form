import os
from dotenv import load_dotenv

load_dotenv()
#environment variables


# Add configuration to factory application.
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI').replace("postgres://", "postgresql://", 1)
SECRET_KEY = os.environ.get('SECRET_KEY')

# Athentication setting
LOGIN_DISABLED = os.environ.get('LOGIN_DISABLED')