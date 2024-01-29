from fastapi import FastAPI

app = FastAPI(title='Proyecto para reseñar peliculas',
              description='En este proyecto se usara para crear reseñas de peliculas.',
              version='1')


@app.get('/')
async def index():
    return 'Hola mundo desde un servidor en FastAPI'
