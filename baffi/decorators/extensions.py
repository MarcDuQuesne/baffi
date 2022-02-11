"""
Decorators to automatize common operations.
"""

from inspect import signature
from functools import wraps
import logging
import pickle as pkl
# TODO import tempfile  # MG permission errors.
from pathlib import Path
import os

from baffi.decorators.core import parametrized

logger = logging.getLogger(__name__)


class NonConstantError(RuntimeError):
    pass


@parametrized
def constants(func, *parameters_to_be_checked, to_disk=False):

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

        before = {key: pkl.dumps(kwargs[key], protocol=pkl.HIGHEST_PROTOCOL) for key in (parameters_to_be_checked or parameters)}

        if to_disk:
            # temp_file = tempfile.NamedTemporaryFile()  # MG this gives permission errors on windows.
            temp_file = Path(os.urandom(32).hex())
            pkl.dump(before, file=temp_file.open(mode='wb'), protocol=pkl.HIGHEST_PROTOCOL)
            del before

        result = func(**kwargs)

        if to_disk:
            before = pkl.load(file=temp_file.open(mode='rb'))
            temp_file.unlink()
            # temp_file.delete()

        for key, serialized_value in before.items():
            if serialized_value != pkl.dumps(kwargs[key], protocol=pkl.HIGHEST_PROTOCOL):
                raise NonConstantError(f"Parameter {key} was modified in function {func.__name__} even if marked as constant using the constants decorator.")

        return result

    return wrapper



