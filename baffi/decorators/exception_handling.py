
from contextlib import contextmanager
from functools import wraps
import logging

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)

@contextmanager
def ignored(*exceptions, loglevel=logging.DEBUG):
    """
    Define a context in which the specified exceptions are ignored.
    """
    try:
        yield
    except exceptions as err:
        logger.log(level=loglevel, msg=f'Ignored exception {err}')
        pass

@parametrized
def return_on_failure(func, value, *exceptions):
    """
    Decorator to return a default value in case of
    an (un)specific exception occurs in the decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with ignored(*(exceptions or [BaseException])):
            return func(*args, **kwargs)
        return value
    return wrapper