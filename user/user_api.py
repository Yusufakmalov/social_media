from fastapi import APIRouter
from user import LoginUserValidator, RegisterUserValidator, EditUserValidator

from database.userservice import (login_user_db, register_user_db, get_exact_user_db,
                                  get_all_users_db)

user_router = APIRouter(prefix='/user', tags=['control users'])


@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    pass


@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    pass


@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    pass