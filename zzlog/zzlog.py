import logging


def setup(
    logger_root,
    level=logging.INFO,
    filename=None,
):
    logger = logging.getLogger(logger_root)
    logger.setLevel(level)

    handler = (
        logging.StreamHandler() if filename is None
        else logging.FileHandler(filename)
    )

    logger.addHandler(handler)

    return logger
