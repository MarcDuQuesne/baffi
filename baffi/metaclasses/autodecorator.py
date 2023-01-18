"""
Interesting metaclasses.
"""


def apply_to_each_function(*decorators):
    """
    Metaclass to apply a decorator to each function in a class.
    """
    class DecoratingMetaclass(type):
        """
        Metaclass to apply a decorator to each function in a class.
        """
        def __new__(cls, class_name, bases, namespace):
            for key, value in list(namespace.items()):
                for decorator in decorators:
                    if callable(value):
                        namespace[key] = decorator(value)
                    elif isinstance(value, classmethod):
                        namespace[key] = classmethod(decorator(value.__func__))
                    elif isinstance(value, staticmethod):
                        namespace[key] = staticmethod(decorator(value.__func__))

            return type.__new__(cls, class_name, bases, namespace)

    return DecoratingMetaclass
