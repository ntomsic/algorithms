"""
Rabin-Miller primality test
returning False implies that n is guaranteed composite
returning True means that n is probably prime
with a 4 ** -k chance of being wrong
"""
import random


def is_prime(_n, k):
    def pow2_factor(num):
        """factor n into a power of 2 times an odd number"""
        power = 0
        while num % 2 == 0:
            num /= 2
            power += 1
        return power, num

    def valid_witness(_a):
        """
        returns true if a is a valid 'witness' for n
        a valid witness increases chances of n being prime
        an invalid witness guarantees n is composite
        """
        _x = pow(int(_a), int(_d), int(_n))

        if _x == 1 or _x == _n - 1:
            return False

        for _ in range(_r - 1):
            _x = pow(int(_x), int(2), int(_n))

            if _x == 1:
                return True
            if _x == _n - 1:
                return False

        return True

    # precondition n >= 5
    if _n < 5:
        return _n == 2 or _n == 3  # True for prime

    _r, _d = pow2_factor(_n - 1)

    for _ in range(k):
        if valid_witness(random.randrange(2, _n - 2)):
            return False

    return True
