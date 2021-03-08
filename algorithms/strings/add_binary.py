"""
Given two binary strings,
return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


def add_binary(_a, _b):
    _s = ""
    _c, i, j = 0, len(_a) - 1, len(_b) - 1
    zero = ord('0')
    while i >= 0 or j >= 0 or _c == 1:
        if i >= 0:
            _c += ord(_a[i]) - zero
            i -= 1
        if j >= 0:
            _c += ord(_b[j]) - zero
            j -= 1
        _s = chr(_c % 2 + zero) + _s
        _c //= 2

    return _s
