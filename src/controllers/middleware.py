from fastapi import Depends, FastAPI, Request, Response
from database import Database
from dependency_injector.wiring import inject, Provide
from inject import Container
from services.logger import Logger
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.orm import Session


@inject
class DBSessionMiddleware(BaseHTTPMiddleware):
  def __init__(
      self, 
      app, 
      dispatch = None, 
      logger : Logger = Depends(Provide[Container.logger]), 
      db : Database = Depends(Provide[Container.db])
    ) -> None:
    super().__init__(app, dispatch)
    self.logger = logger
    self.db : Database = db

  async def dispatch(
      self, 
      request: Request, 
      call_next
    ):
    response : Response = await call_next(request)
    self.logger.info("DB middleware called")
    if 200 <= response.status_code < 400:
      self.db.commit_session()
    else:
      self.db.rollback_session()
    self.db.close_session()
    return response


def setup_middleware(app : FastAPI) -> None:
  app.add_middleware(DBSessionMiddleware)
