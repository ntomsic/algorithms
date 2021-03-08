"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""


def rotate_v1(array, k):
    """
    Rotate the entire array 'k' times
    T(n)- O(nk)

    :type array: List[int]
    :type k: int
    :rtype: void Do not return anything, modify array in-place instead.
    """
    array = array[:]
    _n = len(array)
    for _ in range(k):  # unused variable is not a problem
        temp = array[_n - 1]
        for j in range(_n - 1, 0, -1):
            array[j] = array[j - 1]
        array[0] = temp
    return array


def rotate_v2(array, k):
    """
    Reverse segments of the array, followed by the entire array
    T(n)- O(n)
    :type array: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    array = array[:]

    def reverse(arr, _a, _b):
        while _a < _b:
            arr[_a], arr[_b] = arr[_b], arr[_a]
            _a += 1
            _b -= 1

    _n = len(array)
    k = k % _n
    reverse(array, 0, _n - k - 1)
    reverse(array, _n - k, _n - 1)
    reverse(array, 0, _n - 1)
    return array


def rotate_v3(array, k):
    if array is None:
        return None
    length = len(array)
    k = k % length
    return array[length - k:] + array[:length - k]
