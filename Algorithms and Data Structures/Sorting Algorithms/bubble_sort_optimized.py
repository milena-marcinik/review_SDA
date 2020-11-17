"""
Python program for Optimized implementation of Bubble Sort.

The other optimization we can make leverages the fact that Bubble Sort works in such a way that the largest elements
in a particular iteration end up at the end of the array.

https://stackabuse.com/bubble-sort-in-python/
https://www.geeksforgeeks.org/bubble-sort/
"""


def bubble_sort(array):
    """
    Optimized bubble sort function.

    :param array: given list
    :return: sorted list
    """
    # Gets the length of the array
    length = len(array)
    # flag, check if any swaps were made in the previous iteration
    swapped = True
    num_of_iter = 0

    # if no swaps are made, the algorithm should stop
    while swapped:
        swapped = False
        # with each consecutive iteration we can look at one less element than before
        for i in range(length - num_of_iter - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        num_of_iter += 1


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
