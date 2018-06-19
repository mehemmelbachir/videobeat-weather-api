# VIDEOBEAT BACKEND TEST
Weather API.
==================
The test require to implement a weather measurement service. The initial data incomes in a xlsx
file with the following header: date, time, geoposition coordinates, hight under the ground,
temperature, wind speed, wind vector direction. The initial data needs to be uploaded
through API every minute. The data should be bookkeeped in the service. The algorithm
calculates the service output: average temperature and average wind speed / direction in
space. The algorithm should be scheduled to run every N minutes as a job. The input data and
output results of the service should be accessed through REST API. Caching of the algorithm’s
output should be implemented. The results and statuses of scheduled jobs should be
bookkeeped and accessed through REST API as well.
Requirements: all backend should be written in Python with virtual environment. Database -
mysql. OS - linux. Backend - Django. Caching - Redis. Rest frameform: Django Rest Framework.

<hr/>  

## Configure and run the project.  
Follow these steps to run the project.  

### Main topics:
* [Periodic tasks with django and celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/#periodic-tasks)
* [Caching in django with Redis](https://realpython.com/caching-in-django-with-redis/).
* [Django REST framework](http://www.django-rest-framework.org/).
* [Django and MySQL](https://docs.djangoproject.com/fr/2.0/ref/databases/#mysql-notes)
* [Read xlsx EXCEL 2010+ files with openpyxl](https://openpyxl.readthedocs.io/en/stable/)

### Clone the project:
* Use `git clone 'https://github.com/mehemmelbachir/videobeat-weather-api.git'`

### Create DATABASE:
* open terminal.
* Connect to mysql: </br>
    `mysql -u root -p`.
* Create a database:</br>
`CREATE DATABASE weather_db;`

### Install requirements:
* open terminal
* activate virtual env `path\to\project\env\script\activate`.
* run: `pip install -r requirements.txt`.

### Run DJANGO SERVER
* open terminal
* Activate virtualenv.</br> `path\to\project\env\script\activate`.
* Run DJANGO SERVER:</br>
`python manage.py runserver`.

### Run Celery Sheduled tasks:  
On separated terminals, run the following commands:  
`celery -A weather worker -l info`.  
`celery -A weather beat -l info`.  
**On Windows 10 to fix errors run with __-P eventlet__.**  
`celery -A weather worker -l info -P eventlet`.  
`celery -A weather beat -l info`.  
