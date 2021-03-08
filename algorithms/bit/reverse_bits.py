"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596
(represented in binary as 00000010100101000001111010011100),
return 964176192
(represented in binary as 00111001011110000010100101000000).
"""


def reverse_bits(_n):
    _m = 0
    i = 0
    while i < 32:
        _m = (_m << 1) + (_n & 1)
        _n >>= 1
        i += 1
    return _m
