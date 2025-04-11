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


@app.put('/update_user/{email}/{atrib}/{newvalue}')
async def Update(email: EmailStr, atrib: str, newvalue):
    key = genUUID(email)

    user = data[key]

    newuser = {key: (value if key != atrib else newvalue) for key, value in user.items()}

    data[key] = newuser
    Save(data)

    return JSONResponse(content={'old': user, 'new': newuser}, status_code=200) 


@app.delete('/Delete/{email}')
async def Delete(email):
    return JSONResponse(content={'Deleted': data.pop[genUUID(email)]}, status_code=200)