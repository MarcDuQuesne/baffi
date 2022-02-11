import pytest
import pandas as pd # TODO changeme into something simpler, no need for pandas here.

from baffi.decorators.extensions import constants

@constants
def this_function_does_not_modify_its_arguments(first_arg: list, second_arg: list[str] = ['1']):
    pass


@constants
def this_function_modifies_its_arguments(first_arg: pd.DataFrame, second_arg: list[str] = ['1']):
    second_arg.append(['2'])


@constants
def this_function_reassigns_its_arguments(first_arg: pd.DataFrame, second_arg: list[str] = ['1']):
    first_arg = pd.DataFrame(data=['other'], columns=['df'], index=['very_different'])
    second_arg = []


@pytest.mark.unit
def test_unmodified_parameters_marked_as_costants():
    this_function_does_not_modify_its_arguments(first_arg=pd.DataFrame.from_dict({'1': ['1']}))


@pytest.mark.unit
def test_modified_parameters_marked_as_costants():
    with pytest.raises(RuntimeError) as excinfo:
        this_function_modifies_its_arguments(first_arg=pd.DataFrame.from_dict({'1': ['1']}))
    assert "Parameter second_arg was modified in function this_function_modifies_its_arguments" in str(excinfo.value)


@pytest.mark.unit
def test_rassigned_parameters_marked_as_costants():
    this_function_reassigns_its_arguments(first_arg=pd.DataFrame.from_dict({'1': ['1']}))