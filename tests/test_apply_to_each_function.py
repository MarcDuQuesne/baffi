"""
Test the apply_to_each_function decorator
"""


import pytest

def test_apply_to_each_function():

    def 

    class Foo(dict, metaclass=apply_to_each_function(log_wrapper(level=logging.INFO))):
        def lookup(self, key):
            return self[key]

    d = Foo()
    d["3"] = 2
    d.lookup("3")