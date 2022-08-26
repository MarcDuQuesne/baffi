
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
        pre_format and logger.log(msg=pre_format.format(**locals(), **wrapper_kwargs, **kwargs), level=level)
        result = func(*args, **kwargs)
        post_format and logger.log(msg=post_format.format(**locals(), **wrapper_kwargs, **kwargs), level=level)
        return result
    return wrapper

  
@parametrized
def timeit(
    func,
    format="{func.__name__} executed in {duration:.4f}s",
    level=logging.INFO,
    **wrapper_kwargs,
):
    """
    Logs the execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        duration = t2 - t1  # (t2-t1) won't work with format
        logger.log(
            msg=format.format(**locals(), **wrapper_kwargs, **kwargs), level=level
        )
        return result

    return wrapper
  

@parametrized
def exc_pre_post(func,
                 pre=None,
                 post=None,
                 **wrapper_kwargs
):
    """
    Executes arbitrary functions before and after a given one.
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        _pre = pre(*args, **kwargs, **wrapper_kwargs) if pre else None
        result = func(*args, **kwargs)
        post and post(*args, **kwargs, **wrapper_kwargs, pre=_pre)
        return result

    return wrapper
