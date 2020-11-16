import bisect


def find(nums, num):
    """
    The function uses the bisect library to look for a given number in the list.

    :param nums: list of numbers
    :param num: given number
    :return: return index of first appearance given number in list
    """
    index = bisect.bisect_left(nums, num)
    if index != len(nums) and nums[index] == num:
        return index
    raise ValueError


nums = [1, 2, 3, 3, 3, 6, 6, 8, 10, 10, 10, 10, 10, 15]

# ValueError:
# num = 5
# find(nums, num)

num = 6
print(find(nums, num))
