import uuid


from dal.book_dal import BookDAL
from database import Database
from objects.book import Book


BOOK_SAMPLES = 50000


class BookService():
  def __init__(self, book_dal : BookDAL, db : Database) -> None:
    self.book_dal : BookDAL = book_dal
    print(db)
    self.session = db.session()

  def create_sample_books(self):
    for _ in range(BOOK_SAMPLES):
      id = str(uuid.uuid4())
      book = Book(
        id = id,
        name = f"The {id} book"
      )
      self.book_dal.create_book(book)

  def ping(self) -> str:
    return "pong"
