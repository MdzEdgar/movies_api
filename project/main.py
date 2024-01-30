from fastapi import FastAPI
from database import database as connection
from database import User, Movie, UserReview
from schemas import UserBaseModel

app = FastAPI(title='Proyecto para reseñar peliculas',
              description='En este proyecto se usara para crear reseñas de peliculas.',
              version='1')


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get('/')
async def index():
    return 'Hola mundo desde un servidor en FastAPI'


@app.post('/users')
async def create_user(user: UserBaseModel):

    user = User.create(
        username=user.username,
        password=user.password
    )

    return user.id
