from sqlmodel import select, Session
from db_schema.book_db import Book as DBBook
from objects.book import Book


class BookDAL():
  def create_book(self, session: Session, book: Book) -> Book:
    db_book = DBBook(
      id = book.id,
      name = book.name
    )
    session.add(db_book)
    return book

  def get_book(self, session: Session, id: str) -> Book | None:
    statement = select(DBBook).where(DBBook.id == id)
    result = session.exec(statement).first()
    return result
