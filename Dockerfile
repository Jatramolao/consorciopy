FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip3 install fastapi uvicorn gunicorn sqlalchemy
COPY ./sql_app /main
WORKDIR /main
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]