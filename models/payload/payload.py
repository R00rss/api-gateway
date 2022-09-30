from pydantic import BaseModel


class payloadModel(BaseModel):
    dataType:str
    data:dict