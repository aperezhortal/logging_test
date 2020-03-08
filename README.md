# Test the python logging module

This project implements the logging module in a toy example.

## Usage

pip install git+https://github.com/aperezhortal/logging_test.git

In a python console::

    import logging_test
    from logging_test import my_module 
    
    logging_test.set_loglevel('debug')  # It's info by default
         
    my_module.test_logging()

Output::

    This is a print message
    INFO:logging_test.my_module:This is an info message
    INFO:logging_test.my_module:This is an info message
    DEBUG:logging_test.my_module:This is an info message
    INFO:logging_test.my_module:This is another info message
    INFO:logging_test.my_module:This is another info message
    DEBUG:logging_test.my_module:This is another debug message




