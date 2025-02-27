import logging

def setup_logger(name, log_file='server.log', level=logging.DEBUG):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():  # Prevent adding multiple handlers
        logger.setLevel(level)

        file_handler = logging.FileHandler(log_file)
        stream_handler = logging.StreamHandler()  # Logs to console
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
