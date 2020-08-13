#Archivo de creacion de la base de datos de la API donde se almacenaran los registros de usuario.
#Se utiliza la biblioteca ORM para mapear entre objetos de codigo y tablas de datos (Ej: una clase = una tabla)

#Requeridos para la creacion de una base de datos y la generacion de una sesion
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creacion de la base de datos en el motor "SQLite", donde se conectara a la BD ubicada en "sql_app.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#Creacion del motor de conexion 
#Considerar que por defecto se utiliza un hilo de conexion para cada solicitud. Pero considerando que puede ser necesario utilizar 
#mas de una conexion en distinta, para SQLite se utiliza "check_same_thread" = False.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Al generar una instancia de "SessionLocal" es creara una sesion de SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Devuelve clase, la cual sera heredada para crear los modelos y clases de BD.
Base = declarative_base()