'''

Stooge Sort
Time Complexity : O(n2.709)
Reference: https://www.geeksforgeeks.org/stooge-sort/

'''


def stoogesort(arr, _l, _h):
    if _l >= _h:
        return

    # If first element is smaller
    # than last, swap them
    if arr[_l] > arr[_h]:
        _t = arr[_l]
        arr[_l] = arr[_h]
        arr[_h] = _t

        # If there are more than 2 elements in
    # the array
    if _h - _l + 1 > 2:
        _t = (int)((_h - _l + 1) / 3)

        # Recursively sort first 2 / 3 elements
        stoogesort(arr, _l, (_h - _t))

        # Recursively sort last 2 / 3 elements
        stoogesort(arr, _l + _t, _h)

        # Recursively sort first 2 / 3 elements
        # again to confirm
        stoogesort(arr, _l, (_h - _t))


if __name__ == "__main__":
    array = [1, 3, 64, 5, 7, 8]
    N = len(array)
    stoogesort(array, 0, N - 1)
    for i in range(0, N):
        print(array[i], end=' ')
