"""
Given two strings s1 and s2, determine if s2 is a rotated version of s1.
For example,
is_rotated("hello", "llohe") returns True
is_rotated("hello", "helol") returns False

accepts two strings
returns bool
Reference: https://leetcode.com/problems/rotate-string/description/
"""


def is_rotated(s_1, s_2):
    if len(s_1) == len(s_2):
        return s_2 in s_1 + s_1
    return False


"""
Another solution: brutal force
Complexity: O(N^2)
"""


def is_rotated_v1(s_1, s_2):
    if len(s_1) != len(s_2):
        return False
    if len(s_1) == 0:
        return True

    for _c in range(len(s_1)):
        if all(s_1[(_c + i) % len(s_1)] == s_2[i] for i in range(len(s_1))):
            return True
    return False
