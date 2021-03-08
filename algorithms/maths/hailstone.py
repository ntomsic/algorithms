def hailstone(_n):
    """Return the 'hailstone sequence' from n to 1
       n: The starting point of the hailstone sequence
    """

    sequence = [_n]
    while _n > 1:
        if _n % 2 != 0:
            _n = 3 * _n + 1
        else:
            _n = int(_n / 2)
        sequence.append(_n)
    return sequence
