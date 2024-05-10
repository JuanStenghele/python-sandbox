from sqlalchemy.orm import Session
from database import Database
from objects.book import Book
from db_schema.book_db import Book as DBBook


class BookDAL():
  def __init__(self, db : Database) -> None:
    print(db)
    self.session : Session = db.session()

  def create_book(self, book : Book) -> None:
    db_book = DBBook(
      id = book.id,
      name = book.name
		)
    self.session.add(db_book)
