from fastapi import FastAPI, APIRouter
from .database import database as connection
from .database import User, Movie, UserReview
from .routers import user_router, review_router

app = FastAPI(title='Proyecto para reseñar peliculas',
              description='En este proyecto se usara para crear reseñas de peliculas.',
              version='1')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)

app.include_router(api_v1)


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
