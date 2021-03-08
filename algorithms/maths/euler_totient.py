"""
Euler's totient function, also known as phi-function ϕ(n),
counts the number of integers between 1 and n inclusive,
which are coprime to n.
(Two numbers are coprime if their greatest common divisor (GCD) equals 1).
"""


def euler_totient(_n):
    """Euler's totient function or Phi function.
    Time Complexity: O(sqrt(n))."""
    result = _n
    for i in range(2, int(_n ** 0.5) + 1):
        if _n % i == 0:
            while _n % i == 0:
                _n //= i
            result -= result // i
    if _n > 1:
        result -= result // _n
    return result
