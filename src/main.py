from fastapi import FastAPI
from controllers.book_controller import router as book_router
from controllers.middleware import setup_middleware
from inject import Container


app : FastAPI = FastAPI()
container : Container = Container()
app.container = container

db = app.container.db()
db.create_database()
app.include_router(book_router)
setup_middleware(app)


@app.get("/health-check")
def health_check():
  return {
    "message": "ok"
  }
