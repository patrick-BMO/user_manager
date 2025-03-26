from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import date
from cpf import cpfValidation

class Adress(BaseModel):
    Estado: str = Field(max_length=20)
    Cidade: str = Field(max_length=50)
    Bairro: str = Field(max_length=100)
    Rua: str = Field(max_length=50)
    numero: int


class Cpf(BaseModel):
    cpf: str

    @field_validator('cpf')
    def validar_cpf(cls, value):
        result  = cpfValidation(value)
        if result != value:
            raise result


class User(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    birth: date

    cpf: Cpf
    number: str = Field(pattern=r'^[0-9]{2}[9][0-9]{8}$')
    email: EmailStr

    adress: Adress