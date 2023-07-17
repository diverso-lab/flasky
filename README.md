<div align="center">

  <a href="">[![Pytest Testing Suite](https://github.com/drorganvidez/flask_base/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/drorganvidez/flask_base/actions/workflows/tests.yml)</a>
  <a href="">[![Commits Syntax Checker](https://github.com/drorganvidez/flask_base/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/drorganvidez/flask_base/actions/workflows/commits.yml)</a>
  
</div>

# flask_base

Base project to work with the Python Flask framework in an easy way.

## Set `.env` file in root with:

Create an `.env` file in the root of the project with this information. It is important to obtain a token in Zenodo first.

```
FLASK_APP_NAME=flask_base
MYSQL_HOSTNAME=db
MYSQL_DATABASE=flask_base_db
MYSQL_USER=flask_base_user
MYSQL_PASSWORD=flask_base_pass
MYSQL_ROOT_PASSWORD=flask_base_root_pass
```

## Deploy in develop

To deploy the software under development environment, run:

```
docker compose -f docker-compose.dev.yml up -d 
```

This will apply the migrations to the database and run the Flask application. 

### Migrations

However, if during development there are new changes in the model, run inside the `web` container:

```
flask db migrate
flask db upgrade
```

### Tests

To run unit test, please enter inside `web` container:

```
pytest app/tests/units.py
```

## Deploy in production (Docker Compose)

```
docker compose -f docker-compose.prod.yml up -d 
```
