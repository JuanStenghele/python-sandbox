import pytest, os, psycopg
os.environ["TESTING"] = "true"


from inject import Container
from fastapi.testclient import TestClient
from main import app
from testcontainers.postgres import PostgresContainer
from urllib.parse import urlparse


@pytest.fixture
def db_url():
    with PostgresContainer("postgres:15.3") as postgres:
        yield postgres.get_connection_url()

def insert_book(db, id, name):
    result = urlparse(db)
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port
    with psycopg.connect(
        dbname = database,
        user = username,
        password = password,
        host = hostname,
        port = port
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO books(id, name) VALUES(%s, %s);", (id, name))
            conn.commit()


@pytest.fixture
def data(db_url):
    container = Container()

    mocked_config = {
        "db": {
            "url": db_url
        }
    }

    container.config.override(mocked_config)

    app.container = container
    db = app.container.db()
    db.create_database()

    yield TestClient(app), db_url

    container.unwire()

def test_status(data):
    client, _ = data
    response = client.get("/health-check")
    assert response.status_code == 200
    data = response.json()
    assert data == {
        "message": "ok"
    }

def test_retrieve_book(data):
    client, db_url = data
    insert_book(db_url, '123', 'Harry Potter')
    insert_book(db_url, '456', 'The Lord of the Rings')
    response = client.get("/books", params = { "id": "123" })
    assert response.status_code == 200
    data = response.json()
    assert data == {
        'id': '123',
        'name': 'Harry Potter'
    }

def test_retrieve_unexistent_book(data):
    client, db_url = data
    insert_book(db_url, '123', 'Harry Potter')
    insert_book(db_url, '456', 'The Lord of the Rings')
    response = client.get("/books", params = { "id": "789" })
    assert response.status_code == 200
    data = response.json()
    assert data is None
