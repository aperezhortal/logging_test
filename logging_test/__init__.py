import logging

_logger = logging.getLogger(__name__)

## Functions taken from the matplotlib.__init__ module
def _ensure_handler():
    """
    The first time this function is called, attach a `StreamHandler` using the
    same format as `logging.basicConfig` to the Matplotlib root logger.

    Return this handler every time this function is called.
    """
    global _logger
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    _logger.addHandler(handler)
    return handler


def set_loglevel(level):
    """
    Sets the root logger and root logger handler level, creating
    the handler if it does not exist yet.

    Typically, one should call ``set_loglevel("info")`` or
    ``set_loglevel("debug")`` to get additional debugging information.

    Parameters
    ----------
    level : {"notset", "debug", "info", "warning", "error", "critical"}
        The log level of the handler.

    Notes
    -----
    The first time this function is called, an additional handler is attached
    to root handler; this handler is reused every time and this
    function simply manipulates the logger and handler's level.
    """
    _logger.setLevel(level.upper())
    _ensure_handler().setLevel(level.upper())

# Default level
set_loglevel('info')
