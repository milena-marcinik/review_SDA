"""
Binary Search is an efficient search algorithm that works on sorted arrays.
O(logn)

This search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the
elements after just one comparison.

1) Compare x with the middle element.
2) If x matches with the middle element, we return the mid index.
3) Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid
element. Then we apply the algorithm again for the right half.
4) Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

https://realpython.com/binary-search-python/
https://stackabuse.com/binary-search-in-python/
https://www.geeksforgeeks.org/python-program-for-binary-search/
"""


def find_index(elements, value):
    """
    Iterative Binary Search Function.

    :param elements: given list
    :param value: given value
    :return: returns index of value in given list if present
    """
    # set the lower and the upper boundaries at the opposite ends of the sequence
    low = 0
    high = len(elements) - 1
    # the middle index calculated by taking the average of both boundaries
    mid = (low + high) / 2

    while low <= high:
        # check if value is the element in the middle
        if elements[mid] == value:
            return mid

        # if too small - move the low boundary up
        if elements[mid] < value:
            low = mid + 1
        # if too big - move the high boundary down
        elif elements[mid] > value:
            high = mid - 1

    return -1
