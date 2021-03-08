"""
given an integer, write a function to determine if it is a power of two
"""


def is_power_of_two(_n):
    """
    :type _n: int
    :rtype: bool
    """
    return _n > 0 and not _n & (_n - 1)
