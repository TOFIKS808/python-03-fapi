# Python-03 Fast API

## Description

Fast API serving data from our previosly populated DB

API used https://jsonplaceholder.typicode.com

* PostgreSql
* MariaDB
* Oracle
* MsSQL
* IBM DB2
* SQLite



## Local development with `venv`
* run `make venv` to create `venv`
* run `. ./venv/bin/activate` to activate `venv`
* run `make pip` to install dependencies
* run `make lint` to lint code
* run `make test` to run tests

## Development in Docker
* run `make up`
* open in browser http://127.0.0.1:81 for Jupyter Notebook
* run `make d-pip` to install dependencies in container
* run `make d-lint` to lint code in container
* run `make d-test` to run tests in container


https://medium.com/@arthurapp98/using-sqlalchemy-to-create-and-populate-a-postgresql-database-with-excel-data-eb6049d93402
http://127.0.0.1:8000/docs#/default/users_get_item_users__id__get

ORM relation - delete

https://esmithy.net/2020/06/20/sqlalchemy-cascade-delete/
