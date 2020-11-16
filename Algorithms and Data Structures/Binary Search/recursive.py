"""
Recursive Binary Search Function.
"""


def find_index(elements, low, high, value):
    """
    Recursive Binary Search Function.

    :param elements: given list
    :param low: low boundary, set to 0
    :param high: high boundary, set to len(elements)
    :param value: given value
    :return: returns index of value in given list if present
    """
    if high >= low:
        # the middle index calculated by taking the average of both boundaries
        mid = (low + high) / 2

        # check if element is present at the middle itself
        if elements[mid] == value:
            return mid

        # if too small - move the low boundary up
        if elements[mid] < value:
            return find_index(elements, mid + 1, high, value)
        # if too big - move the high boundary down
        elif elements[mid] > value:
            return find_index(elements, low, mid - 1, value)

    return -1
