import logging
import os

# Create logs directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Shared log file path for all pipeline steps
log_file_path = os.path.join(log_dir, "pipeline.log")

def get_logger(name: str = "pipeline"):
    """
    Returns a logger configured with shared console and file handlers.
    """
    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(logging.DEBUG)

    if not logger_instance.handlers:
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # File Handler
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        logger_instance.addHandler(console_handler)
        logger_instance.addHandler(file_handler)

    return logger_instance

# Single shared logger instance to import directly in all pipeline steps
logger = get_logger("pipeline")


