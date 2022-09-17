def decorating_meta(decorator):
    class DecoratingMetaclass(type):
        def __new__(self, class_name, bases, namespace):
            for key, value in list(namespace.items()):
                if callable(value):
                    namespace[key] = decorator(value)

            return type.__new__(self, class_name, bases, namespace)

    return DecoratingMetaclass


if __name__ == "__main__":

  import logging
  logging.basicConfig(level=logging.DEBUG)

  from baffi.decorators.log_helpers import log_wrapper

  class Foo(dict, metaclass=decorating_meta(log_wrapper(level=logging.INFO))):

    def lookup(self, key):
        return self[key]

  d = Foo()
  d['3'] = 2
  d.lookup('3')

