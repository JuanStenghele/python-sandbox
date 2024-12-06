import time
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from inject import Container
from services.book_service import BookService


router = APIRouter()


@router.get("/books")
@inject
def get_books(
  id : str,
  book_service : BookService = Depends(Provide[Container.book_service])
):
	try:
		return book_service.get_book(id)
	except Exception as e:
		print(str(e))
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/books", response_model = None)
@inject
def create_books(
  book_service : BookService = Depends(Provide[Container.book_service])
):
	try:
		book_service.create_sample_books()
	except Exception as e:
		print(str(e))
		raise HTTPException(detail = "UNKNOWN_ERROR", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
