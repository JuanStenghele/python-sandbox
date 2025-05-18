def build_db_url(user: str, password: str, host: str, port: int, name: str) -> str:
  return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{name}"
