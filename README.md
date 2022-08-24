# student-registration-form

# Introduction
A project that implement **flask-sqlalchemy, flask-login, flask-admin**. Contain simple signup and login feature and also form for registration course



To run the project in your local environment::
```
  1. Clone the repository::

        git clone https://github.com/S-CW/student-registration-form.git

  2. Create and activate a virtual environment::

        virtualenv env -p python3
        source env/bin/activate

  3. Install requirements::

        pip install -r requirements.txt

  4. Run the application::

        run main.py
```  
   
   
Creating database:
```
  1. create .env file
  
  2. Key in:
  
      SQLALCHEMY_DATABASE_URI=
      
      SECRET_KEY=

  3. Initialize database
        
       from website.app import db, create_app
       db.create_all(app=create_app())
```
