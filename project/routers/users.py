from fastapi import HTTPException, APIRouter
from fastapi.security import HTTPBasicCredentials
from ..database import User
from ..schemas import UserResponseModel, UserRequestBaseModel

router = APIRouter(prefix='/users')


@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestBaseModel):
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409, 'El username ya se encuentra en uso.')

    hash_password = User.create_password(user.password)

    user = User.create(
        username=user.username,
        password=hash_password
    )

    return user


@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials):
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(404, 'User not found')

    if user.password != User.create_password(credentials.password):
        raise HTTPException(404, 'Password error')

    return user
