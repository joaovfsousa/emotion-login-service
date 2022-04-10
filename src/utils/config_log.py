import logging


def config_log():
    logging.getLogger().setLevel(logging.INFO)

    if len(logging.getLogger().handlers) > 0:
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)
