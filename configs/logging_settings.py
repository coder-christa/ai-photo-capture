import logging
from .configs import LOG_DIR, LOG_FILE
from pathlib import Path
from datetime import datetime

def setup_logging(BASE_DIR):
    logging.basicConfig(
        filename=Path(BASE_DIR) / (LOG_DIR) / LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s")


def get_current_time():
   return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

