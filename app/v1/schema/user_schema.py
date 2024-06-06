from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="prueba@prueba.cl"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="JCUSERNAME"
    )


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=100,
        example="strongpass"
    )