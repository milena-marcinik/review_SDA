import pytest


@pytest.mark.one
def test_method1():
    a = 6
    b = 9
    assert a == b


@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b

# pytest -v -m two
# restrict a test run to only run tests marked with "two"

# pytest -v -m "not two"
# running all tests except the "two" ones
