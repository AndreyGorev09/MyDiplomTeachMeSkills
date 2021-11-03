![headers](https://github.com/AndreiGorev/diplom/blob/main/assets/headerbank.png)

## Description
_This is a financial project that provides current 
exchange rates and calculates the income on the deposit "On Maru", 
presented on the bank's website "Dabrabyt.by "._

## Languages and Tools

![python](https://img.shields.io/badge/-Python-090909?style=for-the-badge&logo=python&logocolor=00BBBB)
![django](https://img.shields.io/badge/-Django-090909?style=for-the-badge&logo=django&logocolor=00BBBB)
![heroku](https://img.shields.io/badge/-Herku-090909?style=for-the-badge&logo=heroku&logocolor=00BBBB)
![bs4](https://img.shields.io/badge/-BeautifulSoup4-090909?style=for-the-badge&logo=beautifulsoup4&logocolor=00BBBB)
![request](https://img.shields.io/badge/-Request-090909?style=for-the-badge&logo=request&logocolor=00BBBB)
![postgresql](https://img.shields.io/badge/-PostgerSQL-090909?style=for-the-badge&logo=postgresql&logocolor=00BBBB)

## Create the project directory
_you can skip_
* mkdir directory_name
* cd directory_name

## Create and activate your virtualenv
* virtualenv -p python3 .venv
* ...venv/bin/activate

## Installing django
* pip install django

## Create the django project
* django-admin startproject myproject

## Creating the Git repository
* git init 
* Create a file called `.gitignore` with the following content:
```
__pycache__/
.idea
*.sqlite3
.env
.venv
```
* git add .
* git commit -m 'First commit'

## Hidding instance configuration
- create an .env file at the root path and insert the following variables
- SECRET_KEY=Your$eCretKeyHere (Get this secrety key from the settings.py)
- DATABASE=YourDataBAse

### Settings.py
import os
* SECRET_KEY = os.getenv("SECRET_KEY")
* DEBUG = False
* DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite://db.sqlite3"

## Configuring the Data Base (You don't need that if you already had an database).
* pip install dj-database-url

### Settings.py
* import dj_database_url

* DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL),
}


## Static files 

### Settings.py
* include at the MIDDLEWARE in settings.py - 'whitenoise.middleware.WhiteNoiseMiddleware'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIR = []

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

## Create a requirements.txt 
* gunicorn
* psycopg2-binary
* whitenoise
* requests
* heroku
* Delorean
* beautifulsoup4

## Create packages versions requirements.txt
pip freeze > requirements.txt

## Create a file Procfile and add the following code
* web: gunicorn project.wsgi
* release: (cd myproject && python manage.py migrate)

## Creating the app at Heroku
You should install heroku CLI tools in your computer previously ( See http://bit.ly/2jCgJYW ) 
* heroku apps:create app-name (you can create by heroku it's self if you wanted.)
You can also login in heroku by: heroku login
Remember to grab the address of the app in this point

## Setting the allowed hosts
* include all urls at the ALLOWED_HOSTS in settings.py - [*]


## Publishing the app
* git add .
* git commit -m 'Configuring the app'
* git push heroku master 

## Extras

### You may need to disable the collectstatic and install additional configurations
* heroku config:set DISABLE_COLLECTSTATIC=1
* heroku config:set PYTHONPATH=myproject
* heroku config:set SECRET_KEY=Your$eCretKeyHere
* heroku config:set DATABASE_URL=YourDataBase

## Creating the data base (if you are using your own data base you don't need it, if was migrated in the configuration)
* heroku run python manage.py migrate

## Creating the Django admin user
* heroku run python manage.py createsuperuser


