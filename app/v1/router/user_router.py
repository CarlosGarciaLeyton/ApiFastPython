from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.service import auth_service
from app.v1.schema.token_schema import Token

from app.v1.utils.db import get_db

#RUTEO DE URL CON PREFIJO
user_router = APIRouter(
   prefix='/api/v1',

)

@user_router.post(
    "/user",
   tags=["users"],
   summary="Nuevo usuario Creado"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    return user_service.create_user(user)



