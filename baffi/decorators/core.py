
from functools import wraps


def parametrized(decorator):
    """
    Decorator meant to be used by other decorators to provide them with optional arguments.
    """

    @wraps(decorator)
    def wrapper(*args, **kwargs):

        def _decorator_with_arguments(func):
            """ Invoke the original decorator with the arguments. """
            return decorator(func, *args, **kwargs)

        def _decorator_without_arguments():
            """ Invoke the original decorator without arguments. """
            return decorator(args[0])

        if len(args) == 1 and callable(args[0]) and len(kwargs) == 0:
            return _decorator_without_arguments()
        else:
            return _decorator_with_arguments

    return wrapper
