from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from services.logger import Logger


Base = declarative_base()


class Database():
  def __init__(self, url : str, logger : Logger) -> None:
    self.engine = create_engine(url)
    self.session_factory = orm.scoped_session(
      orm.sessionmaker(
        autocommit = False,
        autoflush = True,
        bind = self.engine
      )
    )
    self.current_session : Session | None = None
    self.logger : Logger = logger

  def create_database(self) -> None:
    Base.metadata.create_all(self.engine)
    self.logger.info("DB creation")

  def session(self) -> Session:
    if self.current_session is not None:
      return self.current_session
    self.current_session = self.session_factory()
    self.logger.info("DB new session opened")
    return self.current_session

  def commit_session(self) -> None:
    if self.current_session is None:
      return
    self.current_session.commit()
    self.logger.info("DB session commit")

  def close_session(self) -> None:
    if self.current_session is None:
      return
    self.current_session.close()
    self.current_session = None
    self.logger.info("DB session close")

  def rollback_session(self) -> None:
    if self.current_session is None:
      return
    self.current_session.rollback()
    self.logger.info("DB session rollback")
