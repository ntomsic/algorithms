def gcd(_a, _b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while _b != 0:
        _a, _b = _b, _a % _b
    return _a


def lcm(_a, _b):
    """Computes the lowest common multiple of integers a and b."""
    return _a * _b / gcd(_a, _b)


"""
Given a positive integer x, computes the number of trailing zero of x.
Example
Input : 34(100010)
           ~~~~~^
Output : 1

Input : 40(101000)
           ~~~^^^
Output : 3
"""


def trailing_zero(_x):
    cnt = 0
    while _x and not _x & 1:
        cnt += 1
        _x >>= 1
    return cnt


"""
Given two non-negative integer a and b,
computes the greatest common divisor of a and b using bitwise operator.
"""


def gcd_bit(_a, _b):
    tza = trailing_zero(_a)
    tzb = trailing_zero(_b)
    _a >>= tza
    _b >>= tzb
    while _b:
        if _a < _b:
            _a, _b = _b, _a
        _a -= _b
        _a >>= trailing_zero(_a)
    return _a << min(tza, tzb)
