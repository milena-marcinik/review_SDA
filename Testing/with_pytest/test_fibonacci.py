from .fibinacci import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(6) == 8
    assert fib(8) == 21
