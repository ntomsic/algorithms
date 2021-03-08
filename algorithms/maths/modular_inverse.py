# extended_gcd(a, b) modified from
# https://github.com/keon/algorithms/blob/master/algorithms/maths/extended_gcd.py

def extended_gcd(_a: int, _b: int) -> [int, int, int]:
    """Extended GCD algorithm.
    Return s, t, g
    such that a * s + b * t = GCD(a, b)
    and s and t are co-prime.
    """

    old_s, _s = 1, 0
    old_t, _t = 0, 1
    old_r, _r = _a, _b

    while _r != 0:
        quotient = old_r // _r

        old_r, _r = _r, old_r - quotient * _r
        old_s, _s = _s, old_s - quotient * _s
        old_t, _t = _t, old_t - quotient * _t

    return old_s, old_t, old_r


def modular_inverse(_a: int, _m: int) -> int:
    """
    Returns x such that a * x = 1 (mod m)
    a and m must be coprime
    """

    _s, _, _g = extended_gcd(_a, _m)
    if _g != 1:
        raise ValueError("a and m must be coprime")
    return _s % _m
