"""
Brute Force and Divide and Conquer implementation of
find a max subarray.
"""

import math

lst = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def brute_force(lst):
    """
    Finds the max subarray in lst by nested loops
    and prints the result out
    @param lst: list to search
    @return: None
    """
    start_index = 0
    end_index = 0
    sub_array_sum = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            cur_sum = sum(lst[i:j])
            if cur_sum > sub_array_sum:
                sub_array_sum = cur_sum
                start_index = i
                end_index = j - 1
    print("Brute force Start Index:", start_index,
          "End Index:", end_index, sub_array_sum)


def crossing_subarry(lst, low, mid, high):
    """
    Finds the value of a cross section of the array
    @param lst: the list to search.
    @param low: the lowest index to look at.
    @param mid: the mid-point to use.
    @param high: the highest index to look at.
    @return: The left index, right index, the sum of the
             cross subarray.
    """
    lsum = -math.inf
    cur_sum = 0
    left_index = 0
    for i in range(mid, low - 1, -1):
        cur_sum += lst[i]
        if cur_sum > lsum:
            lsum = cur_sum
            left_index = i
    rsum = -math.inf
    cur_sum = 0
    right_index = 0
    for i in range(mid + 1, high):
        cur_sum += lst[i]
        if cur_sum > rsum:
            rsum = cur_sum
            right_index = i
    return left_index, right_index, lsum + rsum


def divide_and_conquor(lst, low=None, high=None):
    """
    Finds the max subarray using divide and conquer
    @param lst: the list to search.
    @param low: the lowest index to look at.
    @param high: the highest index to look at.
    @return: The left index, right index, the sum of the subarray.
    """
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
    if high == low:
        return low, high, lst[low]
    else:
        mid = (low + high) // 2
        llow, lhigh, lsum = divide_and_conquor(lst, low, mid)
        rlow, rhigh, rsum = divide_and_conquor(lst, mid + 1, high)
        clow, chigh, csum = crossing_subarry(lst, low, mid, high)
        if lsum >= rsum and lsum >= csum:
            return llow, lhigh, lsum
        elif rsum >= lsum and rsum >= csum:
            return rlow, rhigh, rsum
        else:
            return clow, chigh, csum


def linear_max_subarray(lst):
    """
    Uses dynamic programming to find the max subarray in linear
    time

    @param lst: the list to search.
    """
    array = [0] * len(lst)
    array[0] = lst[0]
    start_index = 0
    end_index = 0
    temp_start_index = 0
    temp_end_index = 0
    max_value = lst[0]
    for i in range(1, len(lst)):
        temp_value = array[i - 1] + lst[i]
        if temp_value > lst[i]:
            array[i] = temp_value
            temp_end_index = i
        else:
            array[i] = lst[i]
            temp_start_index = i
        if temp_value > max_value:
            max_value = temp_value
            start_index = temp_start_index
            end_index = temp_end_index
    print("Linear Start Index:", start_index,
          "End Index:", end_index, max_value)


def main():
    """
    Main method to ran program
    @return:
    """
    brute_force(lst)
    linear_max_subarray(lst)
    l, h, s = divide_and_conquor(lst)
    print("Divide and Conquer Start Index:", l, "End Index:", h, s)


main()
