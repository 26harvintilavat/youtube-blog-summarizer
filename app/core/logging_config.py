import logging
from app.core.config import settings

def setup_logging() -> None:
    logging.basicConfig(
        level=(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(messsage)s",
    )