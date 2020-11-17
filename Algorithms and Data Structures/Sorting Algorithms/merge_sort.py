"""
Python program for implementation of Merge Sort.

O(n*log n)

https://www.geeksforgeeks.org/merge-sort/
"""


def merge_sort(array):
    """
    Merge sort function.

    :param array: given list
    :return: sorted list
    """
    length = len(array)
    if length > 1:

        # Finding the mid of the array
        middle = length // 2

        # Dividing the array elements into left and right
        left_arr = array[:middle]
        right_arr = array[middle:]

        # Sorting two parts
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        # Copy data to temp arrays
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1


array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
merge_sort(array)
print(array)
