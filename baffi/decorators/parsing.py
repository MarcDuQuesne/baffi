"""
Decorator to help parsing strings into objects.
"""
from typing import Mapping

objects: Mapping = {}


def register(cls: type) -> type:
    """
    Decorator for objects that registers them in a dictionary.
    """

    objects[cls.__name__.lower()] = cls
    return cls
