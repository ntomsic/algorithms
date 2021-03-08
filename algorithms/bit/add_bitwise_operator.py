"""
The following code adds two positive integers without using the '+' operator.
The code uses bitwise operations to add two numbers.

Input: 2 3
Output: 5
"""


def add_bitwise_operator(_x, _y):
    while _y:
        carry = _x & _y
        _x = _x ^ _y
        _y = carry << 1
    return _x
