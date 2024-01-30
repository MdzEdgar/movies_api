from peewee import *
from decouple import config

DATABASE = config('DB_NAME')

database = MySQLDatabase(config('DB_NAME'),
                         user=config('DB_USER'),
                         password=config('DB_PSWD'),
                         host=config('DB_HOST'),
                         port=config('DB_PORT', cast=int))
