![headers](https://github.com/AndreiGorev/diplom/blob/main/assets/headerbank.png)

## Description

### This is a financial project that provides current exchange rates and calculates the income on the deposit "On Maru", presented on the bank's website "Dabrabyt.by ".

## Languages and Tools

![python](https://img.shields.io/badge/-Python-090909?style=for-the-badge&logo=python&logoColor=00BBBB)
![django](https://img.shields.io/badge/-Django-090909?style=for-the-badge&logo=django&logoColor=00BBBB)
![heroku](https://img.shields.io/badge/-Herku-090909?style=for-the-badge&logo=heroku&logoColor=00BBBB)
![bs4](https://img.shields.io/badge/-BeautifulSoup4-090909?style=for-the-badge&logo=beautifulsoup4&logoColor=00BBBB)
![request](https://img.shields.io/badge/-Request-090909?style=for-the-badge&logo=request&logoColor=00BBBB)
![postgresql](https://img.shields.io/badge/-PostgerSQL-090909?style=for-the-badge&logo=postgresql&logoColor=00BBBB)

## checking whether Python and Pip are installed
* python --version (_PIP is installed with Python by default._)
_For detailed instructions on installing Python, read the topic: (Download and install Python https://pythonru.com/tag/skachat-i-ustanovit-python)._
* python -m pip --version
* python -m pip install --upgrade pip


## Create the project directory
* mkdir directory_name
* cd directory_name

## Create and activate your virtualenv
* virtualenv --version
* pip install virtualenv (_if the version is not presented_)
* virtualenv -p python .venv
* cd .venv\Scripts
* activate 
* where python
* cd ...\directory_name

## Installing Django
* pip install django
* pip freeze

## Clone repository authora
* git clone git@github.com:AndreiGorev/diplom.git
* cd diplom

## Create packages versions requirements.txt
* python -m pip install -r requirements.txt

## Hidding instance configuration
* cd..
* touch .env (save the file in the directory 'directory_name' and insert the following variables)
```
SECRET_KEY=Your$eCretKeyHere 
DATABASE=YourDataBAse
```
## Launching the application
* cd diplom\diplombank
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver






