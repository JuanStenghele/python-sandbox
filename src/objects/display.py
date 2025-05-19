from objects.base import BaseObj
from objects.book import Book


class BookCreationRequest(BaseObj):
  name: str


class BookCreationResponse(BookCreationRequest):
  id: str

  @classmethod
  def from_book(cls, book: Book):
    return cls(
      id = book.id,
      name = book.name
    )
