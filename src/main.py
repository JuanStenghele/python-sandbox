from fastapi import FastAPI
from app import App
from controllers.book_controller import router as book_router
from controllers.middleware import setup_middleware


app : FastAPI = App().get()
App().setup()
app.include_router(book_router)
setup_middleware(App.app)


@app.get("/health-check")
def health_check():
  return {
    "message": "ok"
  }
