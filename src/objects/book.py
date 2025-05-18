from objects.base import OrmObj


class Book(OrmObj):
  id : str
  name : str

  def __init__(self, id : str, name : str):
    super().__init__(
      id = id,
      name = name
    )
