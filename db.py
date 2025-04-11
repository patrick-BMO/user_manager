from uuid import NAMESPACE_URL,  uuid5
from pydantic import BaseModel
import json


def genUUID(email):
        return str(uuid5(NAMESPACE_URL, email))


def Start(filename: str = 'db.json'):
    with open(filename, 'r') as file:
        return json.loads(file.read())


def Save(model: BaseModel | dict, data: dict | None = None,filename: str = 'db.json'):
    if data == None:
        data = Start(filename=filename)

    if type(model) == dict:
          try:
            with open(filename, 'w') as file:
                json.dump(model, file, indent=4)

          except Exception as e:
            print(e)

    else:
        Id = genUUID(model.email)
        data[Id] = model.model_dump()

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(e)

