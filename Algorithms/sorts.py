def insertion_sort(array):
    """
    implementation of insertion sort
    @param array: array to sort
    @return: the sorted array
    """
    if len(array) > 1:
        for i in range(1, len(array)):
            j = i - 1
            while j >= 0 and array[j] > array[j + 1]:
                exchange(array, j + 1, j)
                j -= 1
    return array


def selection_sort(array):
    """
    implementation of selection sort
    @param array: array to sort
    @return: the sorted array
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        exchange(array, min_index, i)
    return array


def merge_sort(array):
    """
    Implementation of merge sort
    @param array: array to sort
    @return: the sorted array
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[0:mid]
    right_array = array[mid:]
    left_sorted = merge_sort(left_array)
    right_sorted = merge_sort(right_array)
    return combine(left_sorted, right_sorted)


def combine(left_array, right_array):
    """
    helper function for the combine portion of the
    merge sort
    @param left_array: sorted left side of the array
    @param right_array: sorted right side of the array
    @return: the two arrays combined and sorted
    """
    lst = list()
    while left_array and right_array:
        if right_array[0] < left_array[0]:
            lst.append(right_array.pop(0))
        else:
            lst.append(left_array.pop(0))
    while left_array:
        lst.append(left_array.pop(0))
    while right_array:
        lst.append(right_array.pop(0))
    return lst


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


def count_sort(array):
    """
    implementation of count sort
    @param array: array to sort
    @return: the sorted array
    """
    if len(array) <= 1:
        return array
    count_array = [0] * max(len(array), max(array))
    for item in array:
        count_array[item] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    result = [0] * len(array)
    for item in array:
        count_array[item] -= 1
        result[count_array[item]] = item
    return result


class Heap:
    def __init__(self):
        """
        Constructor for the heap class
        """
        self.heap_size = None

    @staticmethod
    def parent(i):
        """
        Gets the parent index for i
        @param i: the child to get parent for
        @return: the parent
        """
        return i // 2

    @staticmethod
    def left(i):
        """
        Gets the left child
        @param i: the parent index
        @return: the left child
        """
        return i * 2

    @staticmethod
    def right(i):
        """
        Gets the right child
        @param i: the parent index
        @return: the right child
        """
        return i * 2 + 1

    def max_heapify(self, array, i):
        """
        Heapifies the array
        @param array: the array to heapify
        @param i: the index to start the heapifying
        """
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and array[l - 1] > array[i - 1]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and array[r - 1] > array[largest - 1]:
            largest = r
        if largest != i:
            self.exchange(array, i - 1, largest - 1)
            self.max_heapify(array, largest)

    def build_max_heap(self, array):
        """
        Builds the max heap from array
        @param array: the array to build max heap from
        """
        for i in range(len(array) // 2, 0, -1):
            self.max_heapify(array, i)

    def heapsort(self, array):
        """
        Sorts the array using a heap
        @param array: the array to sort
        @return: the sorted array
        """
        self.heap_size = len(array)
        self.build_max_heap(array)
        for i in range(len(array), 1, -1):
            self.exchange(array, 0, i - 1)
            self.heap_size -= 1
            self.max_heapify(array, 1)
        return array

    def exchange(self, array, i, j):
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
    lst = [2, 8, 7, 1, 3, 5, 6, 4, 9, 5, 2, 1, 3, 4, 4]
    # lst = [1, 4, 1, 2, 6, 5, 2]
    # heap = Heap()
    # lst = heap.heapsort(lst)
    print(lst)
    # lst = [2, 8, 7, 1, 3, 5, 6, 4, 9, 5, 2, 1, 3, 4, 4]
    # lst = merge_sort(lst)
    insertion_sort(lst)
    print(lst)


main()
