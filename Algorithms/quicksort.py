# Implementation of quick sort
import random


def quick_sort(array, start, end):
    """
    implementation of quick sort
    @param array: array of items to sort
    @param start: start index of the array to sort
    @param end: end index of the array to sort
    """
    if start < end:
        mid = partition(array, start, end)
        quick_sort(array, start, mid - 1)
        quick_sort(array, mid + 1, end)


def randomized_quick_sort(array, start, end):
    """
    implementation of randomized quick sort
    @param array: array of items to sort
    @param start: start index of the array to sort
    @param end: end index of the array to sort
    """
    if start < end:
        mid = randomized_partition(array, start, end)
        randomized_quick_sort(array, start, mid - 1)
        randomized_quick_sort(array, mid + 1, end)


def randomized_partition(array, start, end):
    """
    partition the array for randomized quick sort
    @param array: array of items to sort
    @param start: start index of the array to sort
    @param end: end index of the array to sort
    @return: the partion index
    """
    i = random.randint(start, end)
    exchange(array, i, end)
    return partition(array, start, end)


def partition(array, start, end):
    """
    partition the array for quick sort
    @param array: array of items to sort
    @param start: start index of the array to sort
    @param end: end index of the array to sort
    @return: the new partition index
    """
    pivot_value = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot_value:
            i += 1
            exchange(array, i, j)
    exchange(array, i + 1, end)
    return i + 1


def exchange(array, i, j):
    """
    Exchanges the items at index i with index j
    @param array: array of items to sort
    @param i: index of the item to exchange
    @param j: index of the item to exchange
    """
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def main():
    lst = [2, 8, 7, 1, 3, 5, 6, 4]
    lst2 = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(lst, 0, 7)
    randomized_quick_sort(lst2, 0, 7)


main()
