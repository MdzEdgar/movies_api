from peewee import *
from decouple import config
from datetime import datetime

DATABASE = config('DB_NAME')

database = MySQLDatabase(config('DB_NAME'),
                         user=config('DB_USER'),
                         password=config('DB_PSWD'),
                         host=config('DB_HOST'),
                         port=config('DB_PORT', cast=int))


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'


class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'


class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} '

    class Meta:
        database = database
        table_name = 'user_reviews'
