import sys
import logging

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
