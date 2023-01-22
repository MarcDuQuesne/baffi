"""
Test the apply_to_each_function decorator
"""

from functools import wraps

import pytest

from baffi.metaclasses.autodecorator import apply_to_each_function


@pytest.mark.integration
def test_apply_to_each_function():
    """
    Test the apply_to_each_function decorator
    """
    def return_2(func):
        """
        Dummy decorator for the test
        """
        @wraps(func)
        def wrapper(*args, **kwargs):  #pylint: disable=unused-argument
            return 2
        return wrapper

    class Foo(dict, metaclass=apply_to_each_function(return_2)):
        """
        Dummy class for the test
        """
        def return_3(self):
            """
            Dummy function for the test
            """
            return 3

    assert Foo().return_3() == 2, "The function was not applied to the class."
