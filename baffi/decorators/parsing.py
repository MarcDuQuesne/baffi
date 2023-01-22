"""
Decorator to help parsing strings into objects.
"""
from typing import Mapping

classes: Mapping = {}


def register(cls: type) -> type:
    """
    Decorator for classes to register them in a dictionary.
    """

    classes[cls.__name__.lower()] = cls
    return cls
