import pytest


from unittest.mock import MagicMock
from sqlmodel import Session
from objects.book import Book
from dal.book_dal import BookDAL
from sqlmodel import select
from db_schema.book_db import Book as DBBook


class TestBookDal():
  def test_create_book_success(self):
    session_mock = MagicMock(spec = Session)
    book_id = '1'
    book_name = 'Test Book'
    book = Book(id = book_id, name = book_name)
    book_dal = BookDAL()
    result = book_dal.create_book(session_mock, book)
    assert result == book
    added_book = session_mock.add.call_args[0][0]
    assert added_book.id == book_id
    assert added_book.name == book_name

  def test_create_book_fail(self):
    session_mock = MagicMock(spec = Session)
    expected_message = 'Test Exception'
    session_mock.add.side_effect = Exception(expected_message)
    book_id = '1'
    book_name = 'Test Book'
    book = Book(id = book_id, name = book_name)
    book_dal = BookDAL()
    with pytest.raises(Exception) as exc_info:
      book_dal.create_book(session_mock, book)
    assert str(exc_info.value) == expected_message
    assert session_mock.add.call_count == 1

  def test_get_book_success(self):
    session_mock = MagicMock(spec = Session)
    book_id = '1'
    book_name = 'Test Book'
    db_book = DBBook(id = book_id, name = book_name)
    exec_mock = MagicMock()
    exec_mock.first.return_value = db_book
    session_mock.exec.return_value = exec_mock
    book_dal = BookDAL()
    result = book_dal.get_book(session_mock, book_id)
    assert result.id == book_id
    assert result.name == book_name
    assert session_mock.exec.call_count == 1

  def test_get_book_fail(self):
    session_mock = MagicMock(spec = Session)
    expected_message = 'Test Exception'
    session_mock.exec.side_effect = Exception(expected_message)
    book_id = '1'
    book_dal = BookDAL()
    with pytest.raises(Exception) as exc_info:  
      book_dal.get_book(session_mock, book_id)
    assert str(exc_info.value) == expected_message
    assert session_mock.exec.call_count == 1
