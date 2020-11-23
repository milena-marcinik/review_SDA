import pytest


@pytest.fixture
def numbers():
    a = 5
    b = 10
    c = 15
    return [a, b, c]


def test_method1(numbers):
    x = 6
    assert numbers[0] == x


def test_method2(numbers):
    x = 10
    assert numbers[1] == x


def test_method3(numbers):
    x = 15
    assert numbers[2] == x
