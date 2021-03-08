"""
Given two strings S and T, determine if they are both one edit distance apart.
"""


def is_one_edit(_s, _t):
    """
    :type _s: str
    :type _t: str
    :rtype: bool
    """
    if len(_s) > len(_t):
        return is_one_edit(_t, _s)
    if len(_t) - len(_s) > 1 or _t == _s:
        return False
    for i in range(len(_s)):
        if _s[i] != _t[i]:
            return _s[i + 1:] == _t[i + 1:] or _s[i:] == _t[i + 1:]
    return True


def is_one_edit2(_s, _t):
    l_1, l_2 = len(_s), len(_t)
    if l_1 > l_2:
        return is_one_edit2(_t, _s)
    if len(_t) - len(_s) > 1 or _t == _s:
        return False
    for i in range(len(_s)):
        if _s[i] != _t[i]:
            if l_1 == l_2:
                _s = _s[:i] + _t[i] + _s[i + 1:]  # modify
            else:
                _s = _s[:i] + _t[i] + _s[i:]  # insertion
            break
    return _s == _t or _s == _t[:-1]
