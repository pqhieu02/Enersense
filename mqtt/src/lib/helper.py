import logging


def get_default_logging_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)-5s %(name)s: %(message)s'))
    return handler