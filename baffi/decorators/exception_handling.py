"""
Exception handling decorators.
"""
import logging
from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)


@contextmanager
def ignored(*exceptions, loglevel: int = logging.DEBUG, logger: logging.Logger = logger):
    """
    Define a context in which the specified exceptions are ignored.
    """
    try:
        yield
    except exceptions as err:
        loglevel is None or logger.log(level=loglevel, msg=f'Ignored exception {type(err)}.')  # pylint: disable=expression-not-assigned


@parametrized
def return_on_failure(func: Callable, value: Any, *exceptions, loglevel: int = logging.DEBUG, logger: logging.Logger = logger):
    """
    Decorator to return a default value in case of
    an (un)specific exception occurs in the decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with ignored(*(exceptions or [BaseException])):
            return func(*args, **kwargs)
        loglevel is None or logger.log(  # pylint: disable=expression-not-assigned
            level=loglevel,
            msg=f'Encountered exception, {func.__name__} returns the default value: {value}.')
        return value  # pylint: disable=code-unreachable
    return wrapper
