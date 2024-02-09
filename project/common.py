from datetime import datetime
from datetime import timedelta
from decouple import config
import jwt
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = config('SECRET_KEY')
oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')


def create_access_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }

    return jwt.encode(data, SECRET_KEY, algorithm='HS256')
