$ cat CONTRIBUTING.md
# Contributing to the data science code template

Thanks for your interest in my baffi!
## Contributions

I welcome contributions from everyone.
Contributions should be made in the form of pull requests. Each pull request will
be reviewed and either merged in the main branch or given feedback for changes that would be required.


## Pull Request Checklist

- Branch from the main branch and, if needed, rebase to the current main
  branch before submitting your pull request. If it doesn't merge cleanly with
  master you may be asked to rebase your changes.

- Commits should be as small as possible, while ensuring that each commit is
  correct independently.

- Before creating a pull request, please run the test suite (see below) and consider adding new tests if needed.

## Running Tests

I use the `pytest` framework for writing and running tests. 
I provide a `pytest.ini` configuration file in the `tests\` directory alongside the code for the tests themselves.

To run the tests in the current environment, run: `pytest tests\` in the repository root directory.

## Code Formatting

Please make sure to format your code following [PEP8](https://www.python.org/dev/peps/pep-0008/) and
[PEP257](https://www.python.org/dev/peps/pep-0257/).
