import os
from dotenv import load_dotenv

load_dotenv()

# Add configuration to factory application.
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')


# Print out the list of key available in application the environment variable
