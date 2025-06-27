import os


from contextlib import contextmanager
from typing import Generator
from constants import POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD


@contextmanager
def set_env_vars(env_vars: dict[str, str]) -> Generator[None, None, None]:
  old_values = {}
  try:
    for key, value in env_vars.items():
      old_values[key] = os.environ.get(key)
      os.environ[key] = value
    yield
  finally:
    for key, value in old_values.items():
      if value is None:
        del os.environ[key]
      else:
        os.environ[key] = value

def build_env_vars_dict(
  db_host: str,
  db_port: str,
  db_name: str,
  db_user: str,
  db_password: str
) -> dict[str, str]:
  return {
    POSTGRES_DB: db_name,
    POSTGRES_USER: db_user,
    POSTGRES_PASSWORD: db_password,
    POSTGRES_HOST: db_host,
    POSTGRES_PORT: db_port
  }
