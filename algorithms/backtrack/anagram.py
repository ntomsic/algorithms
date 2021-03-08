"""
Given two strings, determine if they are equal after reordering.

Examples:
"apple", "pleap"  -> True
"apple", "cherry" -> False
"""


def anagram(s_1, s_2):
    c_1 = [0] * 26
    c_2 = [0] * 26

    for _c in s_1:
        pos = ord(_c) - ord('a')
        c_1[pos] = c_1[pos] + 1

    for _c in s_2:
        pos = ord(_c) - ord('a')
        c_2[pos] = c_2[pos] + 1

    return c_1 == c_2
