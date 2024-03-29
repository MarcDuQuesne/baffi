## Baffi

A simple collection of python decorators and utils.

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Coverage Status](https://coveralls.io/repos/github/MarcDuQuesne/baffi/badge.svg)](https://coveralls.io/github/MarcDuQuesne/baffi)
![Open Issues](https://img.shields.io/github/issues-raw/MarcDuQuesne/baffi)
![Tests](https://github.com/MarcDuQuesne/baffi/actions/workflows/python-package.yml/badge.svg)

### Overview

#### autoparse_dates
A decorator to automatically parse arguments of supported types from strings to datetime-like objects.
```
    @autoparse_dates('start')
      def some_other_function(start: pd.Timestamp, n_threads: int = 3, end: datetime = '2021-01-05'):
        ...
```

#### return_on_failure
Decorator to return a default value in case of an (un)specific exception occurs in the decorated function.

```
  @return_on_failure('failed', RuntimeError)
    def this_function_fails():
      ...
```

#### constants
Decorator that compares the serialized/unserialized objects being passed as parameters to ensure their value did not change, emulating the const keyword of other languages.

```
@constants
def this_function_does_not_modify_its_arguments(first_arg: list, second_arg: List[str] = ['1']):
    ...
```

#### log_wrapper
Decorator that adds a formatted log line before/after running a function.
Some special variables are available: `func_name` and `results`.
It's also possible to add your own variables.

```
@log_wrapper(pre_format='beginning', post_format='end, result: {result}')
def this_function_returns_something():
    ...
```
