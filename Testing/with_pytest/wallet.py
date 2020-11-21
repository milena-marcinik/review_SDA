class InsufficientAmount(Exception):
    """Exception will be raised when we try to spend more money than we have in the wallet"""
    pass


class Wallet:
    """Application that enables its users to add or spend money in the wallet."""
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def add_cash(self, amount):
        """Method increments the balance with the added amount"""
        self.balance += amount

    def spend_cash(self, amount):
        """"Method reduces the balance by the spent amount, we can’t spend more cash than we have in the wallet."""
        if amount > self.balance:
            raise InsufficientAmount(f"Not enough available to spend {amount}")
        self.balance -= amount


w = Wallet(20)
w.balance