![NECTUS](.vscode/header.svg)

# Nectus :rocket:

Flask Boilerplate to quickly get started with production grade flask application with some additional packages and configuration prebuilt.

## Getting Started

### Prerequisites

-   Python 3.9.2 or higher
-   PostgreSQL
-   Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/Nectus.git

# move to the project folder
$ cd Nectus
```

### Creating virtual environment

-   Install `pipenv` a global python project `pip install pipenv`
-   Create a `virtual environment` for this project

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

### Configuration

-   Create a `.env` file from `.env.sample` and set appropriate environment variables before running the project

```sh
APP_NAME=Nectus

DB_HOST= # Host ex. localhost
DB_DATABASE= # Database
DB_USERNAME= # Username ex. Root
DB_PASSWORD= # Password

JWT_SECRET= # generate a JWT Secret
UPLOAD_FOLDER = public

FLASK_APP=main.py
FLASK_ENV=development
```

### Database Migration

-   Make sure the database name username, password and host have been set in the env

-   Migrate and upgrade database into your database management (for this case postgreeSQL)

```sh
$ flask db init

$ flask db migrate -m "create new table"

$ flask db upgrade
```

### Running app

-   If you feel that everything can be run, then run the Flash API

```sh
$ flask run
```

# Preconfigured Packages

Includes preconfigured packages to kick start flask app by just setting appropriate configuration.

| Package                                                                              | Usage                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| [flask-cors](https://flask-cors.readthedocs.io/)                                     | Configuring CORS                                                               |
| [python-dotenv](https://pypi.org/project/python-dotenv/)                             | Reads the key-value pair from .env file and adds them to environment variable. |
| [PyJWT](https://pyjwt.readthedocs.io/en/stable/)                                           | Python library which allows you to encode and decode JSON Web Tokens (JWT).                |

`autopep8` & `flake8` as `dev` packages for `linting and formatting`

# License

This program is free software under MIT license. Please see the [LICENSE](LICENSE) file in our repository for the full text.
