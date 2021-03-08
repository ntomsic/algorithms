"""

https://en.wikipedia.org/wiki/Bubble_sort

Worst-case performance: O(N^2)

If you call bubble_sort(arr,True), you can see the process of the sort
Default is simulation = False

"""


def bubble_sort(arr, simulation=False):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    _n = len(arr)
    swapped = True

    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)
    _x = -1
    while swapped:
        swapped = False
        _x = _x + 1
        for i in range(1, _n - _x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                if simulation:
                    iteration = iteration + 1
                    print("iteration", iteration, ":", *arr)

    return arr
