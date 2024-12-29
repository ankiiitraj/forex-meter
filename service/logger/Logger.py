import logging
import os

logger = None

def get_logger(name):
    """
    Gets a logger with the given name. Initializes it only once.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The configured logger instance.
    """
    global logger

    if logger is None:
        logger = logging.getLogger(name)
        log_level = os.getenv('LOG_LEVEL', 'INFO')

        logger.setLevel(log_level.upper())

        log_file_path = os.path.join(os.path.dirname(__file__), '../../logs', f'logs.log')
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(log_level.upper()) 

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level.upper())

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger