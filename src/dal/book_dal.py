from sqlmodel import select
from database import Database
from db_schema.book_db import Book as DBBook
from objects.book import Book


class BookDAL():
  def __init__(self, db: Database) -> None:
    self.db = db

  def create_book(self, book: Book) -> Book:
    db_book = DBBook(
      id = book.id,
      name = book.name
    )
    self.db.session().add(db_book)
    return book

  def get_book(self, id: str) -> Book | None:
    statement = select(DBBook).where(DBBook.id == id)
    result = self.db.session().exec(statement).first()
    return result
