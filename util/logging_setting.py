import sys
import logging
from datetime import datetime

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def log_for_func(level='info'):
    def wrapper(func):
        def inner(*args, **kargs):
            if level.lower() == 'debug':
                logging.debug(f'Doing {func.__name__} args:{args[1:]} kargs:{kargs}')
            else:
                logging.info(f'Doing {func.__name__} args:{args[1:]} kargs:{kargs}')

            output = func(*args, **kargs)

            if level.lower() == 'debug':
                logging.debug(f'Completed {func.__name__} args:{args[1:]} kargs:{kargs} result:{output}')
            else:
                logging.info(f'Completed {func.__name__} args:{args[1:]} kargs:{kargs} result:{output}')
            return output
        return inner
    return wrapper

def log_with_time(func):
    start = datetime.now()

    output = func()

    end = datetime.now()
    elapse = end - start
    print(f'Time elapse = {elapse.microseconds / 1000} ms')

    return output