"""
This __init__ module configures the logger.
"""

import logging
from colorlog import ColoredFormatter

# Configure color logging
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)s%(reset)s:\t  %(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Concise timestamp format
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
    reset=True,  # Reset colors after each log message
    style="%",  # Use % formatting style
)

# Create a stream handler to output logs to the console
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Get the root logger and set its level
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # set to DEBUG for more verbose logging


# Clear existing handlers and set the new handler
if logger.hasHandlers():
    logger.handlers.clear()
logger.addHandler(handler)


# Remove the unnecessary info loggers
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)
chromadb_logger = logging.getLogger("chromadb")
chromadb_logger.setLevel(logging.WARNING)
