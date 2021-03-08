"""
Given two strings text and pattern,
return the list of  start indexes in text that matches with the pattern
using knuth_morris_pratt algorithm.
If idx is in the list, text[idx : idx + M] matches with pattern.
Time complexity : O(N+M)
N and M is the length of text and pattern, respectively.
"""


def knuth_morris_pratt(text, pattern):
    _n = len(text)
    _m = len(pattern)
    p_i = [0 for i in range(_m)]
    i = 0
    j = 0
    # making pi table
    for i in range(1, _m):
        while j and pattern[i] != pattern[j]:
            j = p_i[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            p_i[i] = j
    # finding pattern
    j = 0
    ret = []
    for i in range(_n):
        while j and text[i] != pattern[j]:
            j = p_i[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == _m:
                ret.append(i - _m + 1)
                j = p_i[j - 1]
    return ret
