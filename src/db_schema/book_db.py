from database import Base
from sqlalchemy import Column, String


# DB image model
class Book(Base):
  __tablename__ = "books"

  id = Column(String, primary_key = True, index = True)
  name = Column(String, nullable = False)
