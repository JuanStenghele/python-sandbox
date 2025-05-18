from sqlalchemy.orm import Session
from sqlalchemy import text
from database import Database
from logging import Logger


class HealthCheckDAL():
  def __init__(self, db : Database, logger : Logger) -> None:
    self.session : Session = db.session()
    self.logger = logger

  def health_check(self) -> str:
    try:
      self.session.execute(text("SELECT 1"))
      return "ok"
    except Exception as e:
      self.logger.error(f"Error checking postgres database health: {e}")
      return "error"
