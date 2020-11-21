import pytest


# Pytest expects our tests to be located in files whose names begin with test_ or end with _test.py

def capital_case(string):
    if not isinstance(string, str):
        raise TypeError("Provide a string argument")
    return string.capitalize()


def test_capital_case():
    assert capital_case("unicorn") == "Unicorn"


def test_raises_exception_on_non_string_argument():
    with pytest.raises(TypeError):
        capital_case(7)
