# Django_restframwork_project
This project is built with Django and Reset Framework for backend. It is part of the form of a site.

> ## Start of project

 1 . install `venv` in your project file
  ```
 python -m venv .venv_name 
 ```
 2 . Activate `venv`
 ```
 .\venv\Scripts\activate
```
3 . Install the `requirements.txt` file in the project
```
pip install -r  requirements.txt        
```
4 . Create a file named `khadamatikTeta_backend` in the directory `local_settings.py` and set the
necessary settings for the database, etc., similar to the file `local_settings.py.example`.

5 . Connect the project to the database.

► Create migrations 
```
python .\manage.py  makemigrations app_name
```
► Show migrations
```
python .\manage.py  showmigrations
```

► Create tables in database
```
python .\manage.py  migrate 
```
6 . Create an admin account
```
python .\manage.py createsuperuser   
```
7. Run the project server
```
 python .\manage.py  runserver    
 ````

 
