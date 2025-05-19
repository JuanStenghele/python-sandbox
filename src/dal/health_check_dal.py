from sqlmodel import text
from database import Database
from logging import Logger


class HealthCheckDAL():
  def __init__(self, db: Database, logger: Logger) -> None:
    self.db = db
    self.logger = logger

  def health_check(self) -> str:
    try:
      self.db.session().exec(text("SELECT 1"))
      return "ok"
    except Exception as e:
      self.logger.error(f"Error checking postgres database health: {e}")
      return "error"
