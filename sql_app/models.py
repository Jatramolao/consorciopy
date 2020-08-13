#Se importan las clases de la libreria SQLAlchemy para la creacion de las clases/tablas
#asi como de sus relaciones.
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#Se crearan las clases heredando Base del archivo database.py
from database import Base

#Se crea la clase y se declara el nombre de la tabla que se guardara en la base de datos.
#en conjunto con los atributos.

#Tabla Usuario
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
#Relacion con la Tabla Item, donde owner representa un user
    items = relationship("Item", back_populates="owner")

#Tabla Item
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")