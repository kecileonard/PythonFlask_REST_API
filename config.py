import os

#mysql database configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_PORT = "3306"
MYSQL_DB = "flask_rest_api"

#flask config
#'secret key = many random bytes'
SECRET_KEY = os.urandom(24)
