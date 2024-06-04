from fastapi import FastAPI, Form
from typing import List
from uuid import uuid4
from model import Role, User

app = FastAPI()
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
        last_name ="andrea",
        email="jjjj@jjj.cl",
        
    ),
     User(
        id = uuid4(),
        first_name="antonio",
        last_name ="antonio",
        email="jjjj@jjj.cl",
       
    ),

]

@app.get("/api/v1/users")
async def get_users():
    return db










