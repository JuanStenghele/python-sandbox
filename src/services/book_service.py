import uuid


from dal.book_dal import BookDAL
from objects.book import Book


class BookService():
  def __init__(self, book_dal: BookDAL) -> None:
    self.book_dal : BookDAL = book_dal

  def create_book(self, book_name: str) -> Book:
    id = str(uuid.uuid4())
    book = Book(
      id = id,
      name = book_name
    )
    self.book_dal.create_book(book)
    return book

  def get_book(self, id: str) -> Book:
    return self.book_dal.get_book(id)
