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

2) Add to settings.py file:

    import os - in start file

    STATIC_ROOT = '/static/'
    
    STATICFILES_DIRS = [
       os.path.join(BASE_DIR, "static"),
    ]

3) Create directory static

4) Download bootstrap https://getbootstrap.com/docs/5.3/getting-started/download/

5) Copy css, js from bootstrap to static folder

6) Add new app into settings.py file (INSTALLED_APPS)

7) Create file urls.py into test_app directory

8) Modified file urls.py into core directory

9) Create view class

10) Modified file urls.py into app directory



