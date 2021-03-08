"""
Integer base conversion algorithm

int2base(5, 2) return '101'.
base2int('F', 16) return 15.

"""

import string


def int_to_base(_n, base):
    """
        :type _n: int
        :type base: int
        :rtype: str
    """
    is_negative = False
    if _n == 0:
        return '0'
    if _n < 0:
        is_negative = True
        _n *= -1
    digit = string.digits + string.ascii_uppercase
    res = ''
    while _n > 0:
        res += digit[_n % base]
        _n //= base
    if is_negative:
        return '-' + res[::-1]
    return res[::-1]


def base_to_int(_s, base):
    """
        Note : You can use int() built-in function instread of this.
        :type _s: str
        :type base: int
        :rtype: int
    """

    digit = {}
    for i, _c in enumerate(string.digits + string.ascii_uppercase):
        digit[_c] = i
    multiplier = 1
    res = 0
    for _c in _s[::-1]:
        res += digit[_c] * multiplier
        multiplier *= base
    return res
