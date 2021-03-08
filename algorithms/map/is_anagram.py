"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Reference: https://leetcode.com/problems/valid-anagram/description/
"""


def is_anagram(_s, _t):
    """
    :type _s: str
    :type _t: str
    :rtype: bool
    """
    maps = {}
    mapt = {}
    for i in _s:
        maps[i] = maps.get(i, 0) + 1
    for i in _t:
        mapt[i] = mapt.get(i, 0) + 1
    return maps == mapt
