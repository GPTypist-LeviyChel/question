FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./src /app

ENV DB_NAME ...
ENV DB_HOST ...
ENV DB_PORT ...
ENV DB_PASSWORD ...

RUN pip install -r /app/requirements.txt

CMD ["gunicorn", "app.core.main:app", "--bind", "0.0.0.0:80", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]