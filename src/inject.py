from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dal.book_dal import BookDAL
from database import Database
from services.book_service import BookService
from services.logger import Logger


class Container(DeclarativeContainer):
  wiring_config = WiringConfiguration(
    modules = [
      "controllers.book_controller",
      "controllers.middleware"
    ]
  )

  logger = providers.Factory(
    Logger
  )

  db = providers.Singleton(
    Database, 
    url = "postgresql://admin:kzxfngm5ckt2FBH3xef@postgres:5432/db",
    logger = logger
  )

  book_dal = providers.Factory(
    BookDAL,
    db = db
  )

  book_service = providers.Factory(
    BookService,
    book_dal = book_dal,
    db = db
  )
