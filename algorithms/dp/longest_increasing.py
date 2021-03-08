"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Time complexity:
First algorithm is O(n^2).
Second algorithm is O(nlogx) where x is the max element in the list
Third algorithm is O(nlogn)

Space complexity:
First algorithm is O(n)
Second algorithm is O(x) where x is the max element in the list
Third algorithm is O(n)
"""


def longest_increasing_subsequence(sequence):
    """
    Dynamic Programming Algorithm for
    counting the length of longest increasing subsequence
    type sequence: list[int]
    rtype: int
    """
    length = len(sequence)
    counts = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                counts[i] = max(counts[i], counts[j] + 1)
                print(counts)
    return max(counts)


def longest_increasing_subsequence_optimized(sequence):
    """
    Optimized dynamic programming algorithm for
    couting the length of the longest increasing subsequence
    using segment tree data structure to achieve better complexity
    if max element is larger than 10^5 then use
    longest_increasing_subsequence_optimied2() instead
    type sequence: list[int]
    rtype: int
    """
    _max = max(sequence)
    tree = [0] * (_max << 2)

    def update(_p, _l, _r, _i, _v):
        if _l == _r:
            tree[_p] = _v
            return
        mid = (_l + _r) >> 1
        if _i <= mid:
            update(_p << 1, _l, mid, _i, _v)
        else:
            update((_p << 1) | 1, mid + 1, _r, _i, _v)
        tree[_p] = max(tree[_p << 1], tree[(_p << 1) | 1])

    def get_max(_p, _l, _r, _s, _e):
        if _l > _e or _r < _s:
            return 0
        if _l >= _s and _r <= _e:
            return tree[_p]
        mid = (_l + _r) >> 1
        return max(get_max(_p << 1, _l, mid, _s, _e), get_max((_p << 1) | 1, mid + 1, _r, _s, _e))

    ans = 0
    for _x in sequence:
        cur = get_max(1, 0, _max, 0, _x - 1) + 1
        ans = max(ans, cur)
        update(1, 0, _max, _x, cur)
    return ans


def longest_increasing_subsequence_optimized2(sequence):
    """
    Optimized dynamic programming algorithm for
    counting the length of the longest increasing subsequence
    using segment tree data structure to achieve better complexity
    type sequence: list[int]
    rtype: int
    """
    _n = len(sequence)
    tree = [0] * (_n << 2)
    sorted_seq = sorted((x, -i) for i, x in enumerate(sequence))

    def update(_p, _l, _r, _i, _v):
        if _l == _r:
            tree[_p] = _v
            return
        mid = (_l + _r) >> 1
        if _i <= mid:
            update(_p << 1, _l, mid, _i, _v)
        else:
            update((_p << 1) | 1, mid + 1, _r, _i, _v)
        tree[_p] = max(tree[_p << 1], tree[(_p << 1) | 1])

    def get_max(_p, _l, _r, _s, _e):
        if _l > _e or _r < _s:
            return 0
        if _l >= _s and _r <= _e:
            return tree[_p]
        mid = (_l + _r) >> 1
        return max(get_max(_p << 1, _l, mid, _s, _e), get_max((_p << 1) | 1, mid + 1, _r, _s, _e))

    ans = 0
    for _, j in sorted_seq:
        i = -j
        cur = get_max(1, 0, _n - 1, 0, i - 1) + 1
        ans = max(ans, cur)
        update(1, 0, _n - 1, i, cur)
    return ans
