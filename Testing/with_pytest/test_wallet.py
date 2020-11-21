"""
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
"""

import pytest
from .wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """returns wallet instance with balance 0"""
    return Wallet()


@pytest.fixture
def wallet():
    """returns wallet instance with balance 20"""
    return Wallet(20)


@pytest.fixture
def my_wallet():
    """returns a Wallet instance with a zero balance"""
    return Wallet()


# The test function marked with the decorator will then be run once for each set of parameters.
@pytest.mark.parametrize("earned, spent, expected", [(30, 20, 10), (20, 2, 18), (40, 5, 35)])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(90)
    assert wallet.balance == 110


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(50)
