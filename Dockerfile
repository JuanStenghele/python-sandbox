FROM python:3.10

WORKDIR /python-sandbox

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r /python-sandbox/requirements.txt

COPY ./src ./src

CMD ["fastapi", "dev", "/python-sandbox/src/main.py", "--port", "8000", "--host", "0.0.0.0"]
