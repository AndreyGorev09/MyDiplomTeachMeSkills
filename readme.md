![headers](https://github.com/AndreiGorev/diplom/blob/main/assets/headerbank.png)

## Description(local deployment)

### This is a financial project that provides current exchange rates and calculates the income on the deposit "On Maru", presented on the bank's website "Dabrabyt.by ".

## Languages and Tools

![python](https://img.shields.io/badge/-Python-090909?style=for-the-badge&logo=python&logoColor=00BBBB)
![django](https://img.shields.io/badge/-Django-090909?style=for-the-badge&logo=django&logoColor=00BBBB)
![heroku](https://img.shields.io/badge/-Heroku-090909?style=for-the-badge&logo=heroku&logoColor=00BBBB)
![bs4](https://img.shields.io/badge/-BeautifulSoup4-090909?style=for-the-badge&logo=beautifulsoup4&logoColor=00BBBB)
![request](https://img.shields.io/badge/-Request-090909?style=for-the-badge&logo=request&logoColor=00BBBB)
![postgresql](https://img.shields.io/badge/-PostgreSQL-090909?style=for-the-badge&logo=postgresql&logoColor=00BBBB)
![sql](https://img.shields.io/badge/-SQL-090909?style=for-the-badge&logo=sql&logoColor=00BBBB)

## Checking whether Python and Pip are installed
* python3 --version (_PIP is installed with Python by default._)
_For detailed instructions on installing Python, read the topic: (Download and install Python https://pythonru.com/tag/skachat-i-ustanovit-python)._
* python3 -m pip --version (_checking the PIP version_)
* python3 -m pip install --upgrade pip (_you can update PIP if the package is installed_)
_if PIP is not installed:_
* python3 -m pip install -U pip (_install the package for Windows_)
* pip install -U pip (_install the package for Mac, Linux, или Raspberry Pi_)

## Clone repository authora
* git clone git@github.com:AndreiGorev/diplom.git
* cd diplom (_let's go to this directory_)

## Installing packages versions requirements.txt
* python3 -m pip install -r requirements.txt (_install all the packages of their file_)

## Hidding instance configuration
* save the .env file in directory "diplom" and insert the following variables
```
SECRET_KEY=Your$eCretKeyHere 
DATABASE_URL=UrlYourDataBAse 
```
## Launching the application
* cd diplombank/diplombank (_let's go to this directory, in the "settings.py" file change the DEBUG variable to True_)
* cd .. (_venue to the directory above_)
* python3 manage.py migrate (_creating migrations_)
* python3 manage.py createsuperuser (_creating a superuser for the admin panel (optional)_)
* python3 manage.py runserver (_starting a local server_)






