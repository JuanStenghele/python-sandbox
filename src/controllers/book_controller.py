from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from constants import Tags
from inject import Container
from objects.display import BookCreationRequest, BookCreationResponse
from services.book_service import BookService
from logging import Logger


router = APIRouter()


@router.get("/books", tags = [Tags.BOOKS])
@inject
def get_books(
	id: str,
	book_service: BookService = Depends(Provide[Container.book_service]),
	logger: Logger = Depends(Provide[Container.logger])
):
	try:
		return book_service.get_book(id)
	except Exception as e:
		logger.error(f"Error getting book: {e}")
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/books", response_model = BookCreationResponse, tags = [Tags.BOOKS])
@inject
def create_books(
	book: BookCreationRequest,
	book_service: BookService = Depends(Provide[Container.book_service]),
	logger: Logger = Depends(Provide[Container.logger])
):
	try:
		book = book_service.create_book(book.name)
		return BookCreationResponse.from_book(book)
	except Exception as e:
		logger.error(f"Error creating book: {e}")
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
