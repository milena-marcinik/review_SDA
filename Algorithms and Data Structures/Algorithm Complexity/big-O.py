"""
https://pypi.org/project/big-O-calculator/
https://www.inoutcode.com/concepts/big-o/
https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
"""

from bigO import bigO
from random import randint


def quickSort(array):  # in-place | not-stable
    """
    Best : O(nlogn) Time | O(logn) Space
    Average : O(nlogn) Time | O(logn) Space
    Worst : O(n^2) Time | O(logn) Space
    """
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quickSort(smaller) + equal + quickSort(larger)


tester = bigO()
complexity, time = tester.test(quickSort, "random")
