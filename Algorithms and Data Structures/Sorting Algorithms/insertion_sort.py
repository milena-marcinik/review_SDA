"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed
at the correct position in the sorted part.

- An array is partitioned into a "sorted" subarray and an "unsorted" subarray. At the beginning, the sorted subarray
contains only the first element of our original array.

- The first element in the unsorted array is evaluated so that we can insert it into its proper place in the sorted
subarray.

- The insertion is done by moving all elements larger than the new element one position to the right.

- Continue doing this until our entire array is sorted.

O(n^2)

https://www.geeksforgeeks.org/insertion-sort/
https://stackabuse.com/insertion-sort-in-python/
"""


def insertion_sort(array):
    """
    Inserton sort function.

    :param array: given list
    :return: sorted list
    """
    for index in range(1, len(array)):
        current_val = array[index]
        current_pos = index
        while current_pos > 0 and array[current_pos - 1] > current_val:
            array[current_pos] = array[current_pos - 1]
            current_pos = current_pos - 1

        array[index] = current_val


array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
insertion_sort(array)
print(array)
