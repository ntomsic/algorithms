"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Reference: https://leetcode.com/problems/isomorphic-strings/description/
"""


def is_isomorphic(_s, _t):
    """
    :type _s: str
    :type _t: str
    :rtype: bool
    """
    if len(_s) != len(_t):
        return False
    dict = {}
    set_value = set()
    for i in range(len(_s)):
        if _s[i] not in dict:
            if _t[i] in set_value:
                return False
            dict[_s[i]] = _t[i]
            set_value.add(_t[i])
        else:
            if dict[_s[i]] != _t[i]:
                return False
    return True
