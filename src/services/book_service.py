import uuid


from dal.book_dal import BookDAL
from objects.book import Book
from concurrent.futures import ThreadPoolExecutor


BOOK_SAMPLES = 10


class BookService():
  def __init__(self, book_dal : BookDAL) -> None:
    self.book_dal : BookDAL = book_dal

  def create_book(self, book_name : str) -> Book:
    id = str(uuid.uuid4())
    book = Book(
      id = id,
      name = book_name
    )
    self.book_dal.create_book(book)
    return book

  def create_sample_books(self):
    for _ in range(BOOK_SAMPLES):
      id = str(uuid.uuid4())
      book = Book(
        id = id,
        name = f"The {id} book"
      )
      self.book_dal.create_book(book)

  def get_book(self, id : str) -> Book:
    return self.book_dal.get_book(id)

  def get_books(self, search_term : str) -> list:
    return self.book_dal.get_books(search_term)

  def get_books_seq(self, search_terms : list) -> list:
    result = []
    for search_term in search_terms:
      books = self.get_books(search_term)
      result += books
    return result

  def get_books_par(self, search_terms : list) -> list:
    result = []
    with ThreadPoolExecutor() as executor:
      futures = [executor.submit(self.get_books, search_term) for search_term in search_terms]
      for future in futures:
        result += future.result()
    return result