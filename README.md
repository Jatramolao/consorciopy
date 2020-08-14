# ConsorcioProyect
PROYECTO DE API EN PYTHON UTILIZANDO FASTAPI

Sobre el proyecto: 
La API permite la creacion y consulta de usuarios y sus items asociados. El "modelo" usuarios contiene los atributos de "email" y "password".

¿COMO USAR?
Al ingresar a la URL "https://fastapiconsor-y3cfkypqcq-uc.a.run.app/docs" se puede encontrar un modulo de documentacion y de las funciones disponibles para ejecutar (Swagger UI). Las funciones disponibles son:
- GET Users: Metodo para consultar todos los usuarios y sus items.
- POST Users: Metodo para crear un usuario.
- GET Users/user_id: Metodo para consultar el usuario identificado con el "user_id" y sus items.
- POST Users/user_id/Items: Metodo para crear un item perteneciente al usuario "user_id".
- GET Items: Metodo para consultar los items guardados.


GET User:

- Se selecciona el rango de "user_id" a mostrar.
- Salida ejemplo
[
  {
    "email": "Consorcio@consorcio.com",
    "id": 1,
    "is_active": true,
    "items": [
      {
        "title": "PC",
        "description": "PC utilizado para desarrollar apps",
        "id": 1,
        "owner_id": 1
      }
    ]
  }
]

POST User:

- Se ingresan los datos para cada atributo:
{
  "email": "string",
  "password": "string"
}
- Salida ejemplo
{
  "email": "string",
  "id": 0,
  "is_active": true,
  "items": []
}

GET User/user_id:

- Se selecciona el "user_id" a mostrar.
- Salida ejemplo
[
  {
    "email": "Consorcio@consorcio.com",
    "id": 1,
    "is_active": true,
    "items": [
      {
        "title": "PC",
        "description": "PC utilizado para desarrollar apps",
        "id": 1,
        "owner_id": 1
      }
    ]
  }
]



POST Users/{user_id}/Items:

- Se selecciona el "user_id" al cual se le asignarán los atributos del item:
{
  "title": "string",
  "description": "string"
}

- Salida ejemplo
{
  "title": "PC",
  "description": "PC utilizado para desarrollar apps",
  "owner_id": 1
}

- Esta salida contiene un ID para dicho item, según el orden de creación. Ademas, se asigna al "user_id" utilizado.


GET Items:

- Se selecciona el rango de "items_id" a mostrar.
- Salida ejemplo
[
  {
    "title": "string",
    "description": "string",
    "id": 0,
    "owner_id": 0
  }
]

¿COMO INSTALARLO EN MI EQUIPO? primero vamos con los requisitos :

Python:
Se requiere instalar: Python 3.7+ e instalar las librerias fastapi, uvicorn, gunicorn y sqlalchemy.
- Para instalar las librerias (luego de haber instalado python) abrimos una consola y ejecutamos: pip3 install fastapi uvicorn gunicorn sqlalchemy

Con lo anterior (decidido) e instalado, seguimos con:
- Descargar el proyecto y descomprimir en caso de que sea necesario (o aplicamos gitclone al repositorio y evitamos el uso manual).
- Nos ubicamos en la carpeta "sql_app" y abrimos una terminal.
- Ejecutamos: uvicorn main:app --reload.
- ¿Como se que funciono?: aparecen algunas lineas de tipo INFO en la terminal donde debe aparecer el mensaje (comunmente es el ultimo) "Application startup complete". Con esto hacemos click en la direccion
que queda en la consola o ingresamos a http://127.0.0.1:8000/, donde debe aparecer "detail : not found" (No asustarse! Que si levanto el servicio).

Como recomendacion (y una de las virtudes de FastAPI), utilizar el SwaggerUI para probar los metodos de la API (http://127.0.0.1:8000/docs).

¿Y si quiero utilizar Docker?
- Se requiere instalar Docker en alguna de sus versiones y lo ejecutamos.
- Ejecutamos "docker-compose up --build" para crear la imagen, el contenedor y ejecutarlo.
- A diferencia de la version en Python, aqui nos dirigimos al http://localhost y encontraremos el mismo mensaje "detail : not found"

INFORMACION ADICIONAL (y experiencia):
- Si bien, el proyecto se comenzo con la idea de utilizar Flask, por recomendacion de otros colegas, opte por utilizar FastAPI. ¿El motivo? No lo conocia,
se presenta como un recurso moderno y desde un inicio me resulto facil de entender (y replicar).
- Lo mismo ocurre con Docker, ya que si bien, lo conozco y se de que se trata teoricamente, no lo habia llevado a la práctica (y al parecer resulto).
- Los creditos del proyecto API en si van a https://fastapi.tiangolo.com/.
- Por ultimo, el deploy se encuentra automatizado, ya que fue cargado el proyecto de Github y el Dockerfile como proyecto a la nube de Google. A partir de dicho proyecto, se creo un servicio de Google Run para montar el Dockerfile y levantar el entorno.
- En cuanto a un mecanismo de seguridad, Google Run permite correr aplicaciones que incluyen certificado HTTPS.