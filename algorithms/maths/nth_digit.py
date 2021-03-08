def find_nth_digit(_n):
    """find the nth digit of given number.
    1. find the length of the number where the nth digit is from.
    2. find the actual number where the nth digit is from
    3. find the nth digit and return
    """
    length = 1
    count = 9
    start = 1
    while _n > length * count:
        _n -= length * count
        length += 1
        count *= 10
        start *= 10
    start += (_n - 1) / length
    _s = str(start)
    return int(_s[(_n - 1) % length])
