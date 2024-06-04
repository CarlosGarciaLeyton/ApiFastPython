from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    user = "user"       
    bodega = "bodega"

class User (BaseModel):
    id: Optional [UUID]= uuid4() 
    first_name: str
    last_name: str
    email: str
    
    
    


