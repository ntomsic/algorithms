def power(_a: int, _n: int, _r: int = None):
    """
    Iterative version of binary exponentiation

    Calculate a ^ n
    if r is specified, return the result modulo r

    Time Complexity :  O(log(n))
    Space Complexity : O(1)
    """
    ans = 1
    while _n:
        if _n & 1:
            ans = ans * _a
        _a = _a * _a
        if _r:
            ans %= _r
            _a %= _r
        _n >>= 1
    return ans


def power_recur(_a: int, _n: int, _r: int = None):
    """
    Recursive version of binary exponentiation

    Calculate a ^ n
    if r is specified, return the result modulo r

    Time Complexity :  O(log(n))
    Space Complexity : O(log(n))
    """
    if _n == 0:
        ans = 1
    elif _n == 1:
        ans = _a
    else:
        ans = power_recur(_a, _n // 2, _r)
        ans = ans * ans
        if _n % 2:
            ans = ans * _a
    if _r:
        ans %= _r
    return ans
