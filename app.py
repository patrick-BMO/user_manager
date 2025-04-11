from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import EmailStr
from db import Start, Save, genUUID
from models import User

app = FastAPI()
data = Start()

@app.post('/post_user/')
async def Create(user: User):
    Save(user, data)

    return JSONResponse(content=User.model_dump(), status_code=201)


@app.get('/get_user/')
async def Get(email: EmailStr | None = None):
    if email == None:
        return JSONResponse(content=data, status_code=200)
    
    else:
        return JSONResponse(content=data[genUUID(email)], status_code=200)



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