FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip3 install fastapi uvicorn gunicorn sqlalchemy
COPY ./sql_app /apps/sql_app
WORKDIR /apps
CMD ["uvicorn", "sql_app.main:app","--host", "0.0.0.0", "--port", "80"]
ENV port="80"