from sqlmodel import Session, select
from sqlalchemy import literal
from logging import Logger


class HealthCheckDAL():
  def __init__(self, logger: Logger) -> None:
    self.logger = logger

  def health_check(self, session: Session) -> str:
    try:
      session.exec(select(literal(1)))
      return "ok"
    except Exception as e:
      self.logger.error(f"Error checking postgres database health: {e}")
      return "error"
