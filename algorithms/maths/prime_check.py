def prime_check(_n):
    """Return True if n is a prime number
    Else return False.
    """

    if _n <= 1:
        return False
    if _n == 2 or _n == 3:
        return True
    if _n % 2 == 0 or _n % 3 == 0:
        return False
    j = 5
    while j * j <= _n:
        if _n % j == 0 or _n % (j + 2) == 0:
            return False
        j += 6
    return True
