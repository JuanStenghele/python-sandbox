from pydantic import BaseModel


class BaseObj(BaseModel):
  pass


class OrmObj(BaseObj):
  class Config:
    orm_mode = True
