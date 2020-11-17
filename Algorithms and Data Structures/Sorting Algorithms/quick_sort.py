"""
Python program for implementation of QuickSort.

O(n * log n)

https://gist.github.com/anirudhjayaraman/897ca0d97a249180a48b50d62c87f239
https://www.geeksforgeeks.org/python-program-for-quicksort/
https://www.educative.io/edpresso/how-to-implement-quicksort-in-python !!!
"""


def quick_sort(array):
    """
    Quick sort function.

    :param array: given list
    :return: sorted list
    """
    length = len(array)

    # check if array has more than 1 element
    if length >= 2:
        # pick first element as pivot
        pivot = array[0]
        i = 0

        for j in range(length-1):
            if array[j+1] < pivot:
                array[j+1], array[i+1] = array[i+1], array[j+1]
                i += 1

        array[0], array[i] = array[i], array[0]
        first_part = quick_sort(array[:i])
        second_part = quick_sort(array[i+1:])
        first_part.append(array[i])

        return first_part + second_part

    return array


array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
quick_sort(array)
print(array)
