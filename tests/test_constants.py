"""
Tests for the constants decorator.
"""

from typing import List

import pandas as pd  # TODO changeme into something simpler, no need for pandas here.

from baffi.decorators.extensions import constants, NonConstantError

@constants
def this_function_does_not_modify_its_arguments(first_arg: list, second_arg: List[str] = ['1']):
    """
    Test that the constants decorator does not raise an error when a parameter is not modified.
    """


@constants
def this_function_modifies_its_arguments(first_arg: pd.DataFrame, second_arg: List[str] = ['1']):
    """
    Test that the constants decorator raises an error when a parameter is modified.
    """
    second_arg.append(['2'])


@constants(to_disk=True)
def this_function_does_not_modify_its_arguments_fileversion(first_arg: list, second_arg: List[str] = ['1']):
    """
    Test that the constants decorator does not raise an error when a parameter is not modified.
    """


@constants('second_arg', to_disk=True)
def this_function_modifies_its_arguments_fileversion(first_arg: pd.DataFrame, second_arg: List[str] = ['1']):
    """
    Test that the constants decorator raises an error when a parameter is modified.
    """
    second_arg.append(['2'])


@constants
def this_function_reassigns_its_arguments(first_arg: pd.DataFrame, second_arg: List[str] = ['1']):
    """
    Test that the constants decorator does not raise an error when a parameter is reassigned.
    """
    first_arg = pd.DataFrame(data=['other'], columns=['df'], index=['very_different'])
    second_arg = []


@pytest.mark.unit
def test_unmodified_parameters_marked_as_costants():
    """
    Test that the constants decorator does not raise an error when a parameter is not modified.
    """
    this_function_does_not_modify_its_arguments(first_arg=pd.DataFrame.from_dict({'1': ['1']}))


@pytest.mark.unit
def test_modified_parameters_marked_as_costants():
    """
    Test that the constants decorator raises an error when a parameter is modified.
    """
    with pytest.raises(NonConstantError) as excinfo:
        this_function_modifies_its_arguments(first_arg=pd.DataFrame.from_dict({'1': ['1']}))
    assert "Parameter second_arg was modified in function this_function_modifies_its_arguments" in str(excinfo.value)


@pytest.mark.unit
def test_rassigned_parameters_marked_as_costants():
    """
    Test that the constants decorator does not raise an error when a parameter is reassigned.
    """
    this_function_reassigns_its_arguments(first_arg=pd.DataFrame.from_dict({'1': ['1']}))


@pytest.mark.unit
def test_unmodified_parameters_marked_as_costants_fileversion():
    """
    Test that the constants decorator does not raise an error when a parameter is not modified.
    """
    this_function_does_not_modify_its_arguments_fileversion(first_arg=pd.DataFrame.from_dict({'1': ['1']}))


@pytest.mark.unit
def test_modified_parameters_marked_as_costants_fileversion():
    """
    Test that the constants decorator raises an error when a parameter is modified.
    """
    with pytest.raises(NonConstantError) as excinfo:
        this_function_modifies_its_arguments_fileversion(first_arg=pd.DataFrame.from_dict({'1': ['1']}))
    assert "Parameter second_arg was modified in function this_function_modifies_its_arguments" in str(excinfo.value)
