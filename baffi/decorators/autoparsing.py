from contextlib import contextmanager
from functools import wraps
import logging
import datetime
import dateutil
from inspect import signature

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)

@parametrized
def autoparse_dates(func, arguments_names=[]):
    """
    Decorator to automatically parse arguments of supported types from strings to datetime-like objects.
    """

    parse_date_types = {
        datetime: dateutil.parser.parse
    }

    try:
        import pandas as pd
        parse_date_types.update({pd.Timestamp: pd.to_datetime})
    except ImportError:
        logger.warning("Can't import pandas, pd.Timestamp will not be automatically converted.")

    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = signature(func).parameters
        args_names = list(parameters.keys())[0: len(args)]
        kwargs.update({kw: value for kw, value in zip(args_names, args)})
        kwargs.update({kw: parameters[kw].default for kw in set(parameters) - set(kwargs)})
        kwargs.update({kw: parse_date_types[parameters[kw].annotation](value)
                       for kw, value in kwargs.items()
                       if parameters[kw].annotation in parse_date_types and
                       (kw in arguments_names or not arguments_names)})

        return func(**kwargs)

    return wrapper
