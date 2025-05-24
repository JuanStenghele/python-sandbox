from pydantic import BaseModel, ConfigDict


class BaseObj(BaseModel):
  pass


class OrmObj(BaseObj):
  model_config = ConfigDict(from_attributes = True)
