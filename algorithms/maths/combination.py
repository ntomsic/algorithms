def combination(_n, _r):
    """This function calculates nCr."""
    if _n == _r or _r == 0:
        return 1
    return combination(_n - 1, _r - 1) + combination(_n - 1, _r)


def combination_memo(_n, _r):
    """This function calculates nCr using memoization method."""
    memo = {}

    def recur(_n, _r):
        if _n == _r or _r == 0:
            return 1
        if (_n, _r) not in memo:
            memo[(_n, _r)] = recur(_n - 1, _r - 1) + recur(_n - 1, _r)
        return memo[(_n, _r)]

    return recur(_n, _r)
