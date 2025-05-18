FROM python:3.10

WORKDIR /example-api

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r /example-api/requirements.txt

COPY ./src ./src

CMD ["fastapi", "dev", "/example-api/src/main.py", "--port", "8000", "--host", "0.0.0.0"]
