"""

https://en.wikipedia.org/wiki/Pigeonhole_sort

Time complexity: O(n + Range) where n = number of elements and Range = possible values in the array

Suitable for lists where the number of elements and key values are mostly the same.

"""


def pigeonhole_sort(arr):
    _max = max(arr)
    _min = min(arr)
    size = _max - _min + 1

    holes = [0] * size

    for i in arr:
        holes[i - _min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + _min
            i += 1
    return arr
