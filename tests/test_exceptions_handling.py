import pytest

from baffi.decorators.exception_handling import return_on_failure


@return_on_failure('failed', RuntimeError)
def this_function_fails():
    """
    This function fails.
    """
    raise RuntimeError
    return 'never_reached'


@return_on_failure('failed', IndexError)
def this_function_fails_too():
    """
    This function fails, diffrently than before :).
    """
    raise RuntimeError
    return 'never_reached'


@return_on_failure('failed')
def this_function_fails_too_too():
    """
    This function fails
    """
    raise RuntimeError
    return 'never_reached'

@return_on_failure('failed')
def this_function_succedes():
    """
    This function succedes
    """
    return 'succeded'


@pytest.mark.unit
def test_return_on_failure():
    """
    Test the return_on_failure decorator
    """
    value = this_function_fails()
    assert value == 'failed', 'The function does not not return the right value when failing.'

@pytest.mark.unit
def test_return_on_failure_other_exception():
    """
    Test the return_on_failure decorator
    """
    with pytest.raises(RuntimeError):
        this_function_fails_too()

@pytest.mark.unit
def test_another_return_on_failure():
    """
    Test the return_on_failure decorator
    """
    value = this_function_fails_too_too()
    assert value == 'failed', 'The function does not not return the right value when failing.'

@pytest.mark.unit
def test_return_on_failure_succeeds():
    """
    Test the return_on_failure decorator
    """
    value = this_function_succedes()
    assert value == 'succeded', 'The function does not not return the right value when failing.'