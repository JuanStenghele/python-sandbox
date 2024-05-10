from fastapi import FastAPI
from inject import Container


class App():
  app : FastAPI = FastAPI()
  container : Container = Container()

  def setup(self) -> None:
    db = App.container.db()
    db.create_database()
    App.app.container = App.container

  def get_container(self) -> Container:
    return App.container

  def get(self) -> any:
    return App.app
