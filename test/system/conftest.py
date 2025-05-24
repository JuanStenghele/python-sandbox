import pytest


from fastapi.testclient import TestClient
from pytest import FixtureRequest
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs
from constants import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
from utils.env_vars import build_env_vars_dict, set_env_vars


db_name = "db"
db_user = "dev"
db_password = "kzxfngm5ckt2FBH3xef"

class Context():
  def __init__(self, client: TestClient, db_name: str, db_user: str, db_password: str, db_host: str, db_port: int):
    self.client = client
    self.db_name = db_name
    self.db_user = db_user
    self.db_password = db_password
    self.db_host = db_host
    self.db_port = db_port
    self.db_url = f"postgresql+psycopg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

def postgres_instance(request: FixtureRequest) -> tuple[str, int]:
  postgres_container = DockerContainer("postgres:15.3-alpine")
  postgres_container.with_name("test-postgres-db")

  postgres_container.with_exposed_ports(5432)

  postgres_container.with_env(POSTGRES_DB, db_name)
  postgres_container.with_env(POSTGRES_USER, db_user)
  postgres_container.with_env(POSTGRES_PASSWORD, db_password)

  postgres_container.start()

  def remove_container():
    postgres_container.stop()

  request.addfinalizer(remove_container)
  wait_for_logs(postgres_container, r".*database system is ready to accept connections*", timeout = 120)
  return postgres_container.get_container_host_ip(), postgres_container.get_exposed_port(5432)

@pytest.fixture(scope = "session", autouse = True)
def context(request: FixtureRequest):
  db_host, db_port = postgres_instance(request)

  env_vars = build_env_vars_dict(db_host, db_port, db_name, db_user, db_password)
  with set_env_vars(env_vars):
    from inject import Container
    from main import app

    container = Container()

    app.container = container
    db = app.container.db()
    db.create_database()

    yield Context(TestClient(app), db_name, db_user, db_password, db_host, db_port)

  container.unwire()
