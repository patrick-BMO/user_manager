from pydantic import BaseModel, Field, field_validator, EmailStr
from cpf import cpfValidation


class Adress(BaseModel):
    Estado: str = Field(max_length=20)
    Cidade: str = Field(max_length=50)
    Bairro: str = Field(max_length=100)
    Rua: str = Field(max_length=50)
    numero: str = Field(pattern=r'^\d+$')



class User(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    birth: str = Field(pattern=r'^[0-9]{2}[/][0-9]{2}[/][0-9]{4}$')

    cpf: str
    number: str = Field(pattern=r'^[0-9]{2}[9][0-9]{8}$')
    email: EmailStr

    adress: Adress


    @field_validator('cpf')
    def validar_cpf(cls, value):
        result  = cpfValidation(value)
        if result != value:
            raise result
        
        return result