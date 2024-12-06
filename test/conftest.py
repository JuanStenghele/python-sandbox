import os, sys


# Test setup
def pytest_sessionstart(session):
  # Fix the imports
  current_dir = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.join(current_dir, '..', 'src'))
