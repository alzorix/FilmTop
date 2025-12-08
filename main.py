import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from app.ui.console import run_console

if __name__ == "__main__":
    run_console()