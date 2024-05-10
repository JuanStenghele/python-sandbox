RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[34m'
END = '\033[0m'


class Logger():
  # Error messages
  def err(self, msg: str):
    print(f"{RED}[ERROR]{END} - {msg}")

  # Debug messages
  def debug(self, msg: str):
    print(f"{GREEN}[DEBUG]{END} - {msg}")

  # Info messages
  def info(self, msg: str):
    print(f"{BLUE}[INFO]{END} - {msg}")
