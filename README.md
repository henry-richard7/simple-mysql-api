# simple-mysql-api
REST API developed with Python and Flask Framework for Mysql.

# How to use
* Install the dependencies ```pip install -r requirements.txt```
* In the **settings.conf** file add the mysql server details: **hostname**, **user_name**, **password** and **port**.
* Run the app.py by ```python app.py``` in terminal.

# API Domain
By default the api domain is ```http://localhost:5001```

# API endpoints
## database
![GET](https://img.shields.io/badge/GET-26803e) ```/api/database/create```
<br/>
**Parameters**: db_name (The name of the database to create.) [**Required!**]
<br/>
**Example:** http://localhost:5001/api/database/create?db_name=henry_ricks
<br/>
<br/>
**Response**
<br/>
```{"success":true,"msg":f"Database {db_name} Created!."}```
<hr/>

![GET](https://img.shields.io/badge/GET-26803e) ```/api/database/list```
<br/>
**Example:** http://localhost:5001/api/database/list
<br/>
<br/>
**Response**
<br/>
```{"databases":[databases.....]}```
<hr/>

![DELETE](https://img.shields.io/badge/DELETE-b82921) ```/api/database/delete```
<br/>
**Body** 
<br/>
```{"db_name":"the_database_name"}```
<br/>
<br/>
**Response**
<br/>
```{"success":True,"msg":f"Database {db_name} Deleted!."}```

# tables
![GET](https://img.shields.io/badge/GET-26803e) ```/api/tables/list```
<br/>
**Parameters**: db_name (The name of the database to get list of tables.) [**Required!**]
<br/>
**Example:** http://localhost:5001/api/tables/list?db_name=postman_db
<br/>
<br/>
**Response**
<br/>
```{"success":True,"tables":[tables........]}```

# sql
![POST](https://img.shields.io/badge/POST-d97b0f) ```/api/sql/execute```
<br>
**Body**:
<br/>
```{"query":"<THE SQL QUERY>"}```
<br>
<br>
**Response (In Case Of Select Operation)**
<br/>
```{"success":True,"results":[the results.....]}```
<br/>
<br/>
**Response (Other than Select Operation)**
<br/>
```{"success":True,"msg":"Statement executed Successfully"}```

