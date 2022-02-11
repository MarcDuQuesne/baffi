import pytest

from baffi.decorators.exception_handling import return_on_failure


@return_on_failure('failed', RuntimeError)
def this_function_fails():
    raise RuntimeError
    return 'never_reached'

@return_on_failure('failed', IndexError)
def this_function_fails_too():
    raise RuntimeError
    return 'never_reached'

@return_on_failure('failed')
def this_function_fails_too_too():
    raise RuntimeError
    return 'never_reached'

@return_on_failure('failed')
def this_function_succedes():
    return 'succeded'


@pytest.mark.unit
def test_return_on_failure():
    value = this_function_fails()
    assert value == 'failed', 'The function does not not return the right value when failing.'

@pytest.mark.unit
def test_return_on_failure_other_exception():
    with pytest.raises(RuntimeError):
        this_function_fails_too()

@pytest.mark.unit
def test_return_on_failure():
    value = this_function_fails_too_too()
    assert value == 'failed', 'The function does not not return the right value when failing.'

@pytest.mark.unit
def test_return_on_failure_succeeds():
    value = this_function_succedes()
    assert value == 'succeded', 'The function does not not return the right value when failing.'