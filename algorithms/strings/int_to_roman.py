"""
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""


def int_to_roman(num):
    """
    :type num: int
    :rtype: str
    """
    _m = ["", "M", "MM", "MMM"]
    _c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    _x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return _m[num // 1000] + _c[(num % 1000) // 100] + _x[(num % 100) // 10] + i[num % 10]
