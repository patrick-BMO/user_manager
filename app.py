from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    birth: str

    cpf: str = Field(max_length=11)
    number: str
    adress: str
    email: str


with open('db.json', 'r') as db:
    data = db.read()
