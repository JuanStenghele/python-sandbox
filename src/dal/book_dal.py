from sqlalchemy.orm import Session
from database import Database
from objects.book import Book
from db_schema.book_db import Book as DBBook


class BookDAL():
  def __init__(self, db : Database) -> None:
    self.session : Session = db.session()

  def create_book(self, book : Book) -> None:
    db_book = DBBook(
      id = book.id,
      name = book.name
		)
    self.session.add(db_book)

  def get_books(self, search_term : str) -> list:
    query = self.session.query(DBBook)
    query = query.filter(DBBook.name.contains(search_term, autoescape = True))
    return [Book.from_orm(book) for book in query.all()]

  def get_book(self, id : str) -> Book:
    query = self.session.query(DBBook)
    query = query.filter(DBBook.id == id).first()
    if query is None:
      return None
    return Book.from_orm(query)
