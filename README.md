# Epic events

## Description

Epic events is a CRM API with a secure back-end architecture, built in Django Rest framework.  
The user can use the front-end django andmin to connect them and make some operation with their permissions.  


***
## Setup

Create and activate a virtual environnement for the project with Python 3.10.4  
And install the depencies.
    
```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt 
```
## Load data Postgresql
You can use data from the postgreSQL database.   
This database is configured in the settings.py file. Where you can find :    
+ the name of the database 
+ the user
+ the password

```
'NAME': 'epic_event_db',
'USER': 'ludo_user',
'PASSWORD': '123456',
```
And you can load data from the initial_data.json to test the programm:    

```
./manage.py load_data initial_data.json  
```


## Run the server  

Server can be run by this command :
```
python manage.py runserver
```    
and open in browser this adress: [http:/127.0.0.1:8000/]()

## Access to admin
You can acces to the admin interface from this url : http://127.0.0.1:8000/admin  

and with this id of a superuser : 

```
superuser : ludo
pwd : ftwanadoo2
```

***
## Postman documentation
Here the documentation of the Epic event's API: https://documenter.getpostman.com/view/23129255/2s93CPpC7z

***
  

 
