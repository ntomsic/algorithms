import math


def find_order(_a, _n):
    """
    For positive integer n and given integer a that satisfies gcd(a, n) = 1,
    the order of a modulo n is the smallest positive integer k that satisfies
    pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).
    Order of certain number may or may not be exist. If so, return -1.
    """
    if (_a == 1) & (_n == 1):
        return 1
        # Exception Handling: 1 is the order of of 1
    if math.gcd(_a, _n) != 1:
        print("a and n should be relative prime!")
        return -1
    for i in range(1, _n):
        if pow(_a, i) % _n == 1:
            return i
    return -1


def euler_totient(_n):
    """
    Euler's totient function, also known as phi-function ϕ(n),
    counts the number of integers between 1 and n inclusive,
    which are coprime to n.
    (Two numbers are coprime if their greatest common divisor (GCD) equals 1).
    Code from /algorithms/maths/euler_totient.py, written by 'goswami-rahul'
    Time Complexity: O(sqrt(n)).
    """
    result = _n
    for i in range(2, int(_n ** 0.5) + 1):
        if _n % i == 0:
            while _n % i == 0:
                _n //= i
            result -= result // i
    if _n > 1:
        result -= result // _n
    return result


def find_primitive_root(_n):
    """
    For positive integer n and given integer a that satisfies gcd(a, n) = 1,
    a is the primitive root of n, if a's order k for n satisfies k = ϕ(n).
    Primitive roots of certain number may or may not be exist.
    If so, return empty list.
    """
    if _n == 1:
        return [0]
        # Exception Handling: 0 is the only primitive root of 1
    phi = euler_totient(_n)
    p_root_list = []
    # It will return every primitive roots of n.
    for i in range(1, _n):
        if math.gcd(i, _n) != 1:
            continue
            # To have order, a and n must be relative prime with each other.
        order = find_order(i, _n)
        if order == phi:
            p_root_list.append(i)
        else:
            continue
    return p_root_list
