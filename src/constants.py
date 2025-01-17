import os


from enum import Enum


# Config
DEFAULT_CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "config") + "/config.json"

class Tags(Enum):
  HEALTH_CHECK = "Health check"
  BOOKS = "Books"
