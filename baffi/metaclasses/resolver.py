"""
Metaclass resolver to allow multiple metaclasses.
"""

def metaclass_resolver(*classes):
    """
    Resolves inheritance conflicts between metaclasses.
    """
    metaclass = tuple(set(type(cls) for cls in classes))
    metaclass = (
        metaclass[0]
        if len(metaclass) == 1
        else type("_".join(mcls.__name__ for mcls in metaclass), metaclass, {})
    )
    return metaclass("_".join(cls.__name__ for cls in classes), classes, {})
