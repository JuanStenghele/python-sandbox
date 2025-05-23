from sqlalchemy import create_engine, MetaData, delete, insert


def delete_all_books(db_url: str):
  engine = create_engine(db_url)
  metadata = MetaData()
  metadata.reflect(bind = engine)
  books = metadata.tables['books']

  with engine.connect() as connection:
    connection.execute(delete(books))
    connection.commit()

def insert_book(db_url: str, id: str, name: str):
  engine = create_engine(db_url)
  metadata = MetaData()
  metadata.reflect(bind = engine)
  books = metadata.tables['books']

  query = (
    insert(books).values(id = id, name = name)
  )

  with engine.connect() as connection:
    connection.execute(query)
    connection.commit()
