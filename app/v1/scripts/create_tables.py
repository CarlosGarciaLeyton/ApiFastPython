from app.v1.model.user_model import User

from app.v1.utils.db import db

#FUNCION PARA CREAR TABLAS
def create_tables():
    with db:
        db.create_tables([User])
