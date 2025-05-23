import os


from fastapi import FastAPI
from controllers.book_controller import router as book_router
from controllers.health_check import router as health_check_router
from inject import Container
from services.logger import setup_logger
from constants import ENV, ENV_TESTING


setup_logger()

app = FastAPI()
if os.getenv(ENV) != ENV_TESTING:
  container: Container = Container()
  app.container = container
  db = app.container.db()
  db.create_database()

app.include_router(book_router)
app.include_router(health_check_router)
