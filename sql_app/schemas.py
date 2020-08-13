#Se crean los modelos por medio de la libreria pydantic
from typing import List, Optional

from pydantic import BaseModel

#Modelo Base para la Items con sus atributos
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

#Modelo para la creacion de items, considerando los atributos del modelo base
class ItemCreate(ItemBase):
    pass

#Modelo para la lectura de atributos y devolverlos desde la APi para items
class Item(ItemBase):
    id: int
    owner_id: int
#Aqui se declaran configuraciones propias del modelo, de tal manera por medio de 
#Pydantic pueda leer los datos (Considerar que el orm_mode permite que la API pueda
#devolver relaciones).
    class Config:
        orm_mode = True

#Modelo Base para la Items con su atributo
class UserBase(BaseModel):
    email: str

#Modelo para la creacion de users, considerando los atributos del modelo base
class UserCreate(UserBase):
    password: str

#Modelo para la lectura de atributos y devolverlos desde la APi para users
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
#Aqui se declaran configuraciones propias del modelo, de tal manera por medio de 
#Pydantic pueda leer los datos (Considerar que el orm_mode permite que la API pueda
#devolver relaciones).
    class Config:
        orm_mode = True