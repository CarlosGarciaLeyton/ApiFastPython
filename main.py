from fastapi import FastAPI, Form
from typing import List
from uuid import uuid4
from model import Role, User

app = FastAPI(
    title='Apis sistema de x',
    description ="Api que retorna todos los usuarios",
    version ='0.0.1'
)
db: List[User]= [
    User(
        id = uuid4(),
        first_name="jose",
        last_name ="pedro",
        email="jjjj@jj.cl",
       
    ),
     User(
        id = uuid4(),
        first_name="josefa",
        last_name ="andreag",
        email="jjjj@jjj.com",
        
    ),
     User(
        id = uuid4(),
        first_name="antonio",
        last_name ="antonio",
        email="jjjj@jjj.cl",
       
    ),

]

@app.get("/api/v1/user", tags=['inicio'])

async def get_users():
    return db












