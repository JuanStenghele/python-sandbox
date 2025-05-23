from logging import Logger
from typing import Generator
from fastapi import Depends
from sqlmodel import Session
from dependency_injector.wiring import Provide, inject
from inject import Container
from database import Database


@inject
def get_session(
  db: Database = Depends(Provide[Container.db]),
  logger: Logger = Depends(Provide[Container.logger])
) -> Generator[Session, None, None]:
  session = Session(db.engine)
  try:
    logger.info(f"DB session {id(session)} opened")
    yield session
    session.commit()
    logger.info(f"DB session {id(session)} committed")
  except Exception:
    logger.error(f"DB session {id(session)} rollback")
    session.rollback()
    raise
  finally:
    logger.info(f"DB session {id(session)} closing")
    session.close()
