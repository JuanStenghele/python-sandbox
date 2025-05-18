import pytest, os, psycopg
os.environ["TESTING"] = "true"


from inject import Container
from fastapi.testclient import TestClient
from main import app
from testcontainers.postgres import PostgresContainer
from testcontainers.core.waiting_utils import wait_for_logs
from urllib.parse import urlparse
from pytest import FixtureRequest


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


class Context():
    def __init__(self, client : TestClient, db_url : str):
        self.client = client
        self.db_url = db_url


def postgres_instance(request : FixtureRequest) -> str:
    postgres_container = PostgresContainer("postgres:15.3", driver = 'psycopg')

    postgres_container.start()

    def remove_container():
        postgres_container.stop()

    request.addfinalizer(remove_container)
    try:
        wait_for_logs(postgres_container, r".*database system is ready to accept connections.*", timeout = 120)
    except TimeoutError:
        raise TimeoutError("Timeout waiting for Postgres to start")
    return postgres_container.get_connection_url()


@pytest.fixture
def context(request : FixtureRequest):
    db_url = postgres_instance(request)

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

    yield Context(TestClient(app), db_url)

    container.unwire()

def test_status(context : Context):
    client = context.client
    response = client.get("/health-check")
    assert response.status_code == 200
    data = response.json()
    assert data == {
        "message": "ok"
    }

def test_retrieve_book(context : Context):
    db_url = context.db_url
    client = context.client
    insert_book(db_url, '123', 'Harry Potter')
    insert_book(db_url, '456', 'The Lord of the Rings')
    response = client.get("/books", params = { "id": "123" })
    assert response.status_code == 200
    data = response.json()
    assert data == {
        'id': '123',
        'name': 'Harry Potter'
    }

def test_retrieve_unexistent_book(context : Context):
    db_url = context.db_url
    client = context.client
    insert_book(db_url, '123', 'Harry Potter')
    insert_book(db_url, '456', 'The Lord of the Rings')
    response = client.get("/books", params = { "id": "789" })
    assert response.status_code == 200
    data = response.json()
    assert data is None
