import logging
from pathlib import Path

from loguru import logger

from configs import SETTINGS


class _InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        logger.log(level, f"{record.name} - {record.getMessage()}")


def init_logging():
    # Add handlers
    logging.basicConfig(handlers=[_InterceptHandler()], level=0)
    fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"

    # Ensure log directory exists
    log_dir = Path(SETTINGS.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    # ERROR level logs
    logger.add(
        str(log_dir / "log_{time:YYYYMMDD}" / "error.log"),
        format=fmt,
        level="ERROR",
        enqueue=True,
        rotation="50 MB",
        retention="100 week",
        encoding="utf-8",
        compression="zip",
    )

    # INFO level logs
    logger.add(
        str(log_dir / "log_{time:YYYYMMDD}" / "info.log"),
        format=fmt,
        level="INFO",
        enqueue=True,
        rotation="50 MB",
        retention="30 days",
        encoding="utf-8",
        compression="zip",
    )
