"""
Tests for the decorators.
"""

import pandas as pd
from datetime import datetime
import pytest

from baffi.decorators.autoparsing import autoparse_dates


@autoparse_dates
def some_function(start: pd.Timestamp, n_threads: int = 3, end: datetime = '2021-01-05'):
    assert type(start) is pd.Timestamp
    assert type(end) is datetime

@autoparse_dates('start')
def some_other_function(start: pd.Timestamp, n_threads: int = 3, end: datetime = '2021-01-05'):
    assert type(start) is pd.Timestamp
    assert type(end) is str


@pytest.mark.unit
def test_autoparse_wrapper():
    some_function('2017-01-02', n_threads='3', end='2021-06-01')
    some_function(start='2017-01-02')


@pytest.mark.unit
def test_specific_autoparse_wrapper():
    some_other_function('2017-01-02', n_threads='3', end='2021-06-01')
    some_other_function(start='2017-01-02')
