"""
Decorators for logging purposes.
"""

import logging
import os
import sys
from functools import wraps
from inspect import getframeinfo, stack
from time import time

from baffi.decorators.core import parametrized


class OverridingFormatter(logging.Formatter):
    """
    1. Overrides 'funcName' with the value of 'func_name_override', if it exists.
    2. Overrides 'filename' with the value of 'file_name_override', if it exists.
    """

    def format(self, record):
        if hasattr(record, "name_override"):
            record.name = record.name_override
        if hasattr(record, "func_name_override"):
            record.funcName = record.func_name_override
        if hasattr(record, "file_name_override"):
            record.filename = record.file_name_override
        if hasattr(record, "module_override"):
            record.module = record.module_override
        if hasattr(record, "pathname_override"):
            record.pathname = record.pathname_override

        return super(OverridingFormatter, self).format(record)


logger = logging.getLogger(__name__)
logger.propagate = False  # Avoids duplicate messages
handler = logging.StreamHandler(sys.stderr)
format = (
    logging.BASIC_FORMAT
    if logging.root.handlers is None
    else logging.root.handlers[0].formatter._fmt
)  # Taking the first one.
handler.setFormatter(OverridingFormatter(format))
logger.addHandler(handler)


@parametrized
def log_wrapper(
    func,
    pre_format="",
    post_format="{func.__name__}: {result}",
    # logger=None,
    format=None,
    level=logging.INFO,
    **wrapper_kwargs
):
    """
    Decorator that adds a formatted log line before/after running a function
    for debugging purposes.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        py_file_caller = getframeinfo(stack()[1][0])
        extra_args = {
            "name_override": os.path.basename(func.__module__),
            "func_name_override": func.__name__,
            "file_name_override": os.path.basename(py_file_caller.filename),
            "module_name_override": os.path.basename(func.__module__),
            # 'pathname_override':
        }

        start = time()
        pre_format and logger.log(  # pylint: disable=W0106
            msg=pre_format.format(**locals(), **wrapper_kwargs, **kwargs),
            level=level,
            extra=extra_args,
        )
        result = func(*args, **kwargs)
        end = time()
        duration = end - start
        post_format and logger.log(  # pylint: disable=W0106
            msg=post_format.format(**locals(), **wrapper_kwargs, **kwargs),
            level=level,
            extra=extra_args,
        )

        return result

    return wrapper


timeit = log_wrapper(post_format="Duration {duration} s.")


@parametrized
def exc_pre_post(func, pre=None, post=None, **wrapper_kwargs):
    """
    Executes arbitrary functions before and after a given one.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        _pre = pre(*args, **kwargs, **wrapper_kwargs) if pre else None
        result = func(*args, **kwargs)
        post and post(*args, **kwargs, **wrapper_kwargs, pre=_pre)  # pylint: disable=W0106
        return result

    return wrapper
