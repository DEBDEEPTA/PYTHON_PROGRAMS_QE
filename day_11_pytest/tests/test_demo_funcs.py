import pytest

import day_11_pytest.demo_func_to_test as test_func
def test_add():
    result = test_func.add(1,2)
    assert result == 3

def test_divide():
    result = test_func.divide(10,2)
    assert result == 3


def test_divide_exception():
    with pytest.raises(ZeroDivisionError):
        test_func.divide(10,0)