"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""


def missing_ranges(arr, low, high):
    res = []
    start = low

    for _n in arr:

        if _n == start:
            start += 1
        elif _n > start:
            res.append((start, _n - 1))
            start = _n + 1

    if start <= high:  # after done iterating thru array,
        res.append((start, high))  # append remainder to list

    return res
