"""
Interesting metaclasses.
"""


def apply_to_each_function(*decorators):
    class DecoratingMetaclass(type):
        def __new__(self, class_name, bases, namespace):
            for key, value in list(namespace.items()):
                for decorator in decorators:
                    if callable(value):
                        namespace[key] = decorator(value)
                    elif isinstance(value, classmethod):
                        namespace[key] = classmethod(decorator(value.__func__))
                    elif isinstance(value, staticmethod):
                        namespace[key] = staticmethod(decorator(value.__func__))

            return type.__new__(self, class_name, bases, namespace)

    return DecoratingMetaclass


if __name__ == "__main__":

    import logging

    logging.basicConfig(level=logging.DEBUG)

    from baffi.decorators.log_helpers import log_wrapper

    class Foo(dict, metaclass=apply_to_each_function(log_wrapper(level=logging.INFO))):
        def lookup(self, key):
            return self[key]

    d = Foo()
    d["3"] = 2
    d.lookup("3")
