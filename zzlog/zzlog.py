import sys
import logging


def setup(
    logger_root,
    level=logging.INFO,
    filename=None,
    log_exception=True,
):
    logger = logging.getLogger(logger_root)
    logger.setLevel(level)

    handler = (
        logging.StreamHandler() if filename is None
        else logging.FileHandler(filename)
    )

    logger.addHandler(handler)

    if log_exception:
        default_hook = sys.excepthook

        def exception_logger(exc_type, exc_value, exc_traceback):
            if not issubclass(exc_type, KeyboardInterrupt):
                logger.error(
                    'Uncaught exception',
                    exc_info=(exc_type, exc_value, exc_traceback)
                )
            default_hook(exc_type, exc_value, exc_traceback)

        sys.excepthook = exception_logger

    return logger
