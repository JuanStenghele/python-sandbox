from sqlmodel import text, Session
from logging import Logger


class HealthCheckDAL():
  def __init__(self, logger: Logger) -> None:
    self.logger = logger

  def health_check(self, session: Session) -> str:
    try:
      session.exec(text("SELECT 1"))
      return "ok"
    except Exception as e:
      self.logger.error(f"Error checking postgres database health: {e}")
      return "error"
