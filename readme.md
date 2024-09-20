1) Start project commands:

    -python3 -m venv .venv
   
    -source .venv/bin/activate
   
    -pip install django
   
    -django-admin startproject core
   
    -cd core
   
    -python manage.py startapp test_app
   
    -python manage.py runserver 0.0.0.0:8000

    -python manage.py makemigrations
   
    -python manage.py migrate

3) Add to settings.py file:

    import os - in start file

    STATIC_ROOT = '/static/'
    
    STATICFILES_DIRS = [
       os.path.join(BASE_DIR, "static"),
    ]

4) Create directory static

5) Download bootstrap https://getbootstrap.com/docs/5.3/getting-started/download/

6) Copy css, js from bootstrap to static folder

7) Add new app into settings.py file (INSTALLED_APPS)

8) Create file urls.py into test_app directory

9) Modified file urls.py into core directory

10) Create view class

11) Modified file urls.py into app directory



