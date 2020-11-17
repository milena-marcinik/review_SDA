"""
Python program for implementation of Bubble Sort
https://stackabuse.com/bubble-sort-in-python/
https://www.geeksforgeeks.org/bubble-sort/
"""


def bubble_sort(array):
    """
    Bubble sort function.

    :param array: given list
    :return: sorted list
    """
    # Gets the length of the array
    length = len(array)

    for num in range(length):
        for i in range(length - 1):
            # Swap if the element found is greater than the next element
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
