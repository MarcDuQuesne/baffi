"""
Decorators to automatize common operations.
"""

from inspect import signature
from functools import wraps
import logging
import pickle as pkl

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)


@parametrized
def constants(func, *parameters_to_be_checked):

    """
    Decorator that compares the serialized/unserialized objects being passed as parameters
    to ensure their value did not change, emulating the const keyword of other languages.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = signature(func).parameters
        args_names = list(parameters.keys())[0: len(args)]
        kwargs.update({kw: value for kw, value in zip(args_names, args)})
        kwargs.update({kw: parameters[kw].default for kw in set(parameters) - set(kwargs)})
        before = {key: pkl.dumps(kwargs[key], protocol=pkl.HIGHEST_PROTOCOL) for key in (parameters_to_be_checked or list(parameters.keys()))}
        result = func(**kwargs)
        for key, string_representation in before.items():
            if string_representation != pkl.dumps(kwargs[key], protocol=pkl.HIGHEST_PROTOCOL):
                raise RuntimeError(f"Parameter {key} was modified in function {func.__name__} even if marked as constant using the constants decorator.")
        return result

    return wrapper



