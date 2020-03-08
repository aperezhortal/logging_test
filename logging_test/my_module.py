import logging

_logger = logging.getLogger(__name__)


def test_logging():
    print('This is a print message')
    _logger.info('This is an info message')
    _logger.debug('This is an info message')
    _logger.info('This is another info message')
    _logger.debug('This is another debug message')
