from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import user_schema
from app.v1.service import user_service

from app.v1.utils.db import get_db
#RUTEO DE URL CON PREFIJO
router = APIRouter(
    prefix="/api/v1",
    tags=["USER"]
)


@router.post(
    "/user/",
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Nuevo usuario Creado"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Create USER

    ### Args
    La web recibe parametros, que son devueltos en objeto Usuario
    - email: un email valido
    - username: un unico username
    - password: una password fuerte

    ### Returns
    - user: info del usuario
    """
    return user_service.create_user(user)
