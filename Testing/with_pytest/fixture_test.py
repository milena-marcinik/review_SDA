"""
https://docs.pytest.org/en/latest/skipping.html
"""

import pytest


@pytest.fixture
def numbers():
    a = 5
    b = 10
    c = 15
    return [a, b, c]


# This test will run but no traceback will be reported when it fails. Instead, terminal reporting will list it in the
# “expected to fail”
@pytest.mark.xfail
def test_method1(numbers):
    x = 6
    assert numbers[0] == x


# The simplest way to skip a test function is to mark it with the skip decorator which may be passed an optional reason:
@pytest.mark.skip(reason="no way of currently testing this")
def test_method2(numbers):
    x = 10
    assert numbers[1] == x


def test_method3(numbers):
    x = 15
    assert numbers[2] == x
