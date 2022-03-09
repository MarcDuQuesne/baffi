
from functools import wraps
import logging

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)


@parametrized
def log_wrapper(func,
                pre_format='',
                post_format='{func.__name__}: {result}',
                level=logging.INFO,
                **wrapper_kwargs):
    """
    Decorator that adds a formatted log line before/after running a function
    for debugging purposes.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        pre_format and logger.log(msg=pre_format.format(**locals(), **wrapper_kwargs), level=level)
        result = func(*args, **kwargs)
        post_format and logger.log(msg=post_format.format(**locals(), **wrapper_kwargs), level=level)
        return result
    return wrapper
