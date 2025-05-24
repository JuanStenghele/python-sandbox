from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from sqlmodel import Session
from constants import Tags
from inject import Container
from objects.display import BookCreationRequest, BookCreationResponse
from services.book_service import BookService
from logging import Logger
from controllers.dependencies import get_session


router = APIRouter()


@router.get("/books", tags = [Tags.BOOKS])
@inject
def get_books(
	id: str,
	book_service: BookService = Depends(Provide[Container.book_service]),
	session: Session = Depends(get_session),
	logger: Logger = Depends(Provide[Container.logger])
):
	try:
		book = book_service.get_book(session, id)
	except Exception as e:
		logger.error(f"Error getting book: {e}")
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
	if book is None:
		raise HTTPException(detail = "BOOK_NOT_FOUND", status_code = status.HTTP_404_NOT_FOUND)
	return book


@router.post("/books", response_model = BookCreationResponse, tags = [Tags.BOOKS])
@inject
def create_books(
	book: BookCreationRequest,
	book_service: BookService = Depends(Provide[Container.book_service]),
	session: Session = Depends(get_session),
	logger: Logger = Depends(Provide[Container.logger])
):
	try:
		book = book_service.create_book(session, book.name)
		return BookCreationResponse.from_book(book)
	except Exception as e:
		logger.error(f"Error creating book: {e}")
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
