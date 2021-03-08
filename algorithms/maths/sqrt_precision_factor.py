"""
Given a positive integer N and a precision factor P,
it produces an output
with a maximum error P from the actual square root of N.

Example:
Given N = 5 and P = 0.001, can produce output x such that
2.235 < x < 2.237. Actual square root of 5 being 2.236.
"""


def square_root(_n, epsilon=0.001):
    """Return square root of n, with maximum absolute error epsilon"""
    guess = _n / 2

    while abs(guess * guess - _n) > epsilon:
        guess = (guess + (_n / guess)) / 2

    return guess
