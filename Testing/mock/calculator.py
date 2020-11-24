"""
https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
"""

import time


class Calculator:
    def summary(self, a, b):
        time.sleep(5)  # long running process
        return a + b


