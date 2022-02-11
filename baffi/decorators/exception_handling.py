
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
        loglevel is None or logger.log(level=loglevel, msg=f'Ignored exception {type(err)}.')
        pass

@parametrized
def return_on_failure(func, value, *exceptions, loglevel=logging.DEBUG):
    """
    Decorator to return a default value in case of
    an (un)specific exception occurs in the decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with ignored(*(exceptions or [BaseException])):
            return func(*args, **kwargs)
        loglevel is None or logger.log(level=loglevel, msg=f'Encountered exception, {func.__name__} returns the default value: {value}.')
        return value
    return wrapper