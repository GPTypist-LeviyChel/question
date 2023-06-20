from structlog import getLogger


def get_logger(context: dict = None):
    logger = getLogger()

    if context:
        logger = logger.bind(**context)

    return logger
