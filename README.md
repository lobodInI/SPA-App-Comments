# SPA-App-Comments

## Installing using GitHub

Install PostgresSQL and create db
```angular2html
git clone https://github.com/lobodInI/SPA-App-Comments/tree/develop
cd spa_comments
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

set DB_HOST=&laquo;your db hostname&raquo;
set DB_NAME=&laquo;your db name&raquo;
set DB_USER=&laquo;your db username&raquo;
set DB_PASSWORD=&laquo;your db user password&raquo;
set SECRET_KEY=&laquo;your secret key&raquo;

python manage.py migrate
python manage.py runserver
```

## Run with docker

Docker should be installed
```angular2html
docker compose build
docker compose up
```

## Getting access

* create user via /api/user/register/
* get access token via /api/user/token/
* download ModHeader extension for your browser
* create request header via access token in ModHeader extension


## API Documentation
For detailed API documentation:

- Redoc: http://127.0.0.1:8000/api/doc/redoc/
- Swagger UI: http://127.0.0.1:8000/api/doc/swagger/