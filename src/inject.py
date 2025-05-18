from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dal.book_dal import BookDAL
from database import Database
from services.book_service import BookService
from services.logger import Logger
from utils.database import build_db_url
from constants import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_HOST_DEFAULT, POSTGRES_PORT_DEFAULT


class Container(DeclarativeContainer):
  wiring_config = WiringConfiguration(
    modules = [
      "controllers.book_controller",
      "controllers.health_check",
      "controllers.middleware"
    ]
  )

  config = providers.Configuration()

  # DB configuration
  config.db.name.from_env(POSTGRES_DB)
  config.db.user.from_env(POSTGRES_USER)
  config.db.password.from_env(POSTGRES_PASSWORD)
  config.db.host.from_env(POSTGRES_HOST, default = POSTGRES_HOST_DEFAULT)
  config.db.port.from_env(POSTGRES_PORT, default = POSTGRES_PORT_DEFAULT)

  logger = providers.Factory(
    Logger
  )

  db_url = providers.Callable(
    build_db_url,
    user = config.db.user,
    password = config.db.password,
    host = config.db.host,
    port = config.db.port,
    name = config.db.name
  )

  db = providers.Singleton(
    Database, 
    url = db_url,
    logger = logger
  )

  book_dal = providers.Factory(
    BookDAL,
    db = db
  )

  book_service = providers.Factory(
    BookService,
    book_dal = book_dal
  )
