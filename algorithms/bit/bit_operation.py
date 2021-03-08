"""
Fundamental bit operation:
    get_bit(num, i): get an exact bit at specific index
    set_bit(num, i): set a bit at specific index
    clear_bit(num, i): clear a bit at specific index
    update_bit(num, i, bit): update a bit at specific index
"""


def get_bit(num, i):
    """
    This function shifts 1 over by i bits, creating a value being like 0001000. By
    performing an AND with num, we clear all bits other than the bit at bit i.
    Finally we compare that to 0
    """
    return (num & (1 << i)) != 0


def set_bit(num, i):
    """
    This function shifts 1 over by i bits, creating a value being like 0001000. By
    performing an OR with num, only value at bit i will change.
    """
    return num | (1 << i)


def clear_bit(num, i):
    """
    This method operates in almost the reverse of set_bit
    """
    mask = ~(1 << i)
    return num & mask


def update_bit(num, i, bit):
    """
    To set the ith bit to value, we first clear the bit at position i by using a
    mask. Then, we shift the intended value. Finally we OR these two numbers
    """
    mask = ~(1 << i)
    return (num & mask) | (bit << i)
