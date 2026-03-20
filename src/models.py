from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: int
    name: str