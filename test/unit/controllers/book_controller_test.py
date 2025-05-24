import pytest


from unittest.mock import MagicMock
from fastapi import HTTPException
from objects.display import BookCreationRequest
from services.book_service import BookService
from sqlalchemy.orm import Session
from logging import Logger


class TestBookController():
  def test_create_book_500_error(self):
    from controllers.book_controller import create_books
    book = BookCreationRequest(name = 'Harry Potter')
    book_service_mock = MagicMock(spec = BookService)
    book_service_mock.create_book.side_effect = Exception('error')
    session_mock = MagicMock(spec = Session)
    logger_mock = MagicMock(spec = Logger)
    with pytest.raises(HTTPException) as e:
      create_books(
        book = book, 
        book_service = book_service_mock,
        session = session_mock,
        logger = logger_mock
      )
    assert e.value.status_code == 500
    assert e.value.detail == 'UNKNOWN_ERROR'
    assert book_service_mock.create_book.call_count == 1

  def test_get_book_500_error(self):
    from controllers.book_controller import get_books
    book_service_mock = MagicMock(spec = BookService)
    book_service_mock.get_book.side_effect = Exception('error')
    session_mock = MagicMock(spec = Session)
    logger_mock = MagicMock(spec = Logger)
    with pytest.raises(HTTPException) as e:
      get_books(
        id = '123', 
        book_service = 
        book_service_mock, 
        session = session_mock, 
        logger = logger_mock
      )
    assert e.value.status_code == 500
    assert e.value.detail == 'UNKNOWN_ERROR'
    assert book_service_mock.get_book.call_count == 1
