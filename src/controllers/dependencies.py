from logging import Logger
from typing import Generator
from fastapi import Depends
from sqlmodel import Session
from inject import Container
from database import Database


def get_session(
  db: Database = Depends(lambda: Container.db()),
  logger: Logger = Depends(lambda: Container.logger())
) -> Generator[Session, None, None]:
  session = Session(db.engine)
  logger.info(f"DB session {id(session)} opened")
  try:
    yield session
    session.commit()
    logger.info(f"DB session {id(session)} committed")
  except Exception:
    session.rollback()
    logger.info(f"DB session {id(session)} rollback")
    raise
  finally:
    session.close()
    logger.info(f"DB session {id(session)} closed")
