"""
Test for the register decorator
"""
import pytest

from baffi.decorators.parsing import classes, register


@pytest.mark.unit
def test_register():
    """
    Test the register decorator
    """

    @register
    class Foo:
        """
        Dummy class for the test
        """

    assert classes['foo'] == Foo, "The class was not registered."
