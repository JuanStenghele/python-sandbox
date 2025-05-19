from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from constants import Tags
from inject import Container
from objects.display import BookCreationRequest, BookCreationResponse
from services.book_service import BookService


router = APIRouter()


@router.get("/books", tags = [Tags.BOOKS])
@inject
def get_books(
	id: str,
	book_service: BookService = Depends(Provide[Container.book_service])
):
	try:
		return book_service.get_book(id)
	except Exception as e:
		print(str(e))
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/books", response_model = BookCreationResponse, tags = [Tags.BOOKS])
@inject
def create_books(
	book: BookCreationRequest,
	book_service: BookService = Depends(Provide[Container.book_service])
):
	try:
		book = book_service.create_book(book.name)
		return BookCreationResponse.from_book(book)
	except Exception as e:
		print(str(e))
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
