"""
Given an array and a number k
Find the max elements of each of its sub-arrays of length k.

Keep indexes of good candidates in deque d.
The indexes in d are from the current window, they're increasing,
and their corresponding nums are decreasing.
Then the first deque element is the index of the largest window value.

For each index i:

1. Pop (from the end) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the front) the index i - k, if it's still in the deque
   (it falls out of the window).
4. If our window has reached size k,
   append the current window maximum to the output.
"""

import collections


def max_sliding_window(arr, k):
    q_i = collections.deque()  # queue storing indexes of elements
    result = []
    for i, _n in enumerate(arr):
        while q_i and arr[q_i[-1]] < _n:
            q_i.pop()
        q_i.append(i)
        if q_i[0] == i - k:
            q_i.popleft()
        if i >= k - 1:
            result.append(arr[q_i[0]])
    return result
