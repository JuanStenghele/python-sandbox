from sqlmodel import create_engine, SQLModel
from logging import Logger


class Database():
  def __init__(self, url : str, logger : Logger) -> None:
    self.engine = create_engine(url)
    self.logger : Logger = logger

  def create_database(self) -> None:
    SQLModel.metadata.create_all(self.engine)
    self.logger.info("DB creation")
