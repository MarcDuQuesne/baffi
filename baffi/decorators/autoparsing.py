from contextlib import contextmanager
from functools import wraps
import logging
import datetime
import dateutil
from inspect import signature

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)

@parametrized
def autoparse_dates(func, *arguments_names, log_level=logging.DEBUG):
    """
    Decorator to automatically parse arguments of supported types from strings to datetime-like objects.
    """

    parse_date_types = {
        datetime.datetime: dateutil.parser.parse
    }

    try:
        import pandas as pd
        parse_date_types.update({pd.Timestamp: pd.to_datetime})
    except ImportError:
        logger.warning("Can't import pandas, pd.Timestamp will not be automatically converted.")

    def _log_and_parse(argument_name, argument_value, parsing_function):
        """A simple wrapper to also add a line of logs"""
        logger.log(msg=f'Autoparsing argument with name {argument_name} and value {argument_value}.', level=log_level)
        return parsing_function(argument_value)

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Performs the conversion (considering the default values) and invokes the function"""
        parameters = signature(func).parameters
        args_names = list(parameters.keys())[0: len(args)]
        kwargs.update({kw: value for kw, value in zip(args_names, args)})
        kwargs.update({kw: parameters[kw].default for kw in set(parameters) - set(kwargs)})
        kwargs.update({kw: _log_and_parse(argument_name=kw,
                                          argument_value=value,
                                          parsing_function=parse_date_types[parameters[kw].annotation])
                       for kw, value in kwargs.items()
                       if parameters[kw].annotation in parse_date_types and
                       (kw in arguments_names or not arguments_names)})

        return func(**kwargs)

    return wrapper
