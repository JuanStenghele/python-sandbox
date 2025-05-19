import os


from contextlib import asynccontextmanager
from fastapi import FastAPI
from controllers.book_controller import router as book_router
from controllers.health_check import router as health_check_router
from controllers.middleware import setup_middleware
from inject import Container
from services.logger import setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
  setup_logger()

  if os.getenv("TESTING") != "true":
    container: Container = Container()
    app.container = container
    db = app.container.db()
    db.create_database()
  yield

app = FastAPI(lifespan = lifespan)
setup_middleware(app)

app.include_router(book_router)
app.include_router(health_check_router)
