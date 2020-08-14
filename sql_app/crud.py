#Aqui se describen las funciones para la iteraccion con la base de datos: Crear, Leer, Actualizar y Eliminar
#para este caso, solo se disponen de funciones para la creacion y consulta.
#Ademas, se importan la libreria de SQLalchemy para vincular las sesiones y cada una de las funciones.
from sqlalchemy.orm import Session

#import models 
#import schemas
from . import models,schemas

#Por medio de la fucion query() se realizar las diferentes consultas (lectura) sobre la base de datos
#para cada una de las funciones declaradas.

#Funciones de consulta para Usuarios
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


#Funcion para la creacion de usuarios
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user) #Generar instancia del modelo.
    db.commit()     #Generar cambio en la BD a partir del modelo instanciado.
    db.refresh(db_user) #Generar refresh de la instancia para disponer de los nuevos datos.
    return db_user


#Funciones de consulta para Items
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

#Funcion para la creacion de Items
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item) #Generar instancia del modelo.
    db.commit()      #Generar cambio en la BD a partir del modelo instanciado.
    db.refresh(db_item) #Generar refresh de la instancia para disponer de los nuevos datos.
    return db_item