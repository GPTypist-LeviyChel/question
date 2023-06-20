FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY src /app/src/

CMD ["gunicorn", "src.core.main:app", "--bind", "0.0.0.0:8080", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]