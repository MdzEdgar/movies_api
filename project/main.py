from fastapi import FastAPI
from database import database as connection

app = FastAPI(title='Proyecto para reseñar peliculas',
              description='En este proyecto se usara para crear reseñas de peliculas.',
              version='1')


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        print('Connecting...')


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Close')


@app.get('/')
async def index():
    return 'Hola mundo desde un servidor en FastAPI'
