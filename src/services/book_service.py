import uuid


from dal.book_dal import BookDAL
from objects.book import Book
from sqlmodel import Session


class BookService():
  def __init__(self, book_dal: BookDAL) -> None:
    self.book_dal: BookDAL = book_dal

  def create_book(self, session: Session, book_name: str) -> Book:
    id = str(uuid.uuid4())
    book = Book(
      id = id,
      name = book_name
    )
    self.book_dal.create_book(session, book)
    return book

  def get_book(self, session: Session, id: str) -> Book | None:
    return self.book_dal.get_book(session, id)
