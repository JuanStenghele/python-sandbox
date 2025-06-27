from sqlmodel import SQLModel, Field


class Book(SQLModel, table = True):
  __tablename__: str = "books"
  
  id: str = Field(primary_key = True, index = True)
  name: str = Field(nullable = False)
