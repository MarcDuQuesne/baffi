"""
Test for the register decorator
"""
import pytest

from baffi.decorators.parsing import objects, register


@pytest.mark.unit
def test_register():
    """
    Test the register decorator
    """

    @register
    class Foo:  # pylint: disable=too-few-public-methods
        """
        Dummy class for the test
        """

    @register
    def bar():  # pylint: disable=disallowed-name
        """
        Dummy function for the test
        """

    assert objects['foo'] == Foo, "The class was not registered."
    assert objects['bar'] == bar, "The function was not registered."  # pylint: disable=comparison-with-callable
