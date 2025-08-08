from enum import Enum


# Env contants
ENV = "ENV"
ENV_TESTING = "test"

# DB constants
POSTGRES_DB = "POSTGRES_DB"
POSTGRES_USER = "POSTGRES_USER"
POSTGRES_PASSWORD = "POSTGRES_PASSWORD"
POSTGRES_HOST = "POSTGRES_HOST"
POSTGRES_PORT = "POSTGRES_PORT"
POSTGRES_HOST_DEFAULT = "postgres"
POSTGRES_PORT_DEFAULT = 5432

# Logger
LOGGER_NAME = "python-sandbox"

class Tags(Enum):
  HEALTH_CHECK = "Health check"
  BOOKS = "Books"
