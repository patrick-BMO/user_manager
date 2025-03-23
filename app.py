from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    birth: date

    cpf: str = Field(max_length=11)
    number: str
    adress: str
    email: str
