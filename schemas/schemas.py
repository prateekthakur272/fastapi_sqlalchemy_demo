from pydantic import BaseModel

class NotePydanticIn(BaseModel):
    title:str
    description:str

class NotePydanticOut(BaseModel):
    id:int
    title:str
    description:str
    
    class Config:
        from_attributes=True
