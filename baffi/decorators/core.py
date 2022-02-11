




def parametrized(decorator):
    """
    Decorator meant to be used by other decorators to provide them with arguments.
    """
    def wrapped_decorator(*args, **kwargs):
        if len(args) == 1 and callable(args[0]) and len(kwargs) == 0:
            return decorator(args[0])
        else:
            def real_decorator(decoratee):
                return decorator(decoratee, *args, **kwargs)

            return real_decorator

    return wrapped_decorator