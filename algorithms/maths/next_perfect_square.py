"""
This program will look for the next perfect square.
Check the argument to see if it is a perfect square itself,
if it is not then return -1 otherwise look for the next perfect square
for instance if you pass 121 then the script should return the next perfect square which is 144.
"""


def find_next_square(sqr):
    root = sqr ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1


# Another way:

def find_next_square2(sqr):
    _x = sqr ** 0.5
    return -1 if _x % 1 else (_x + 1) ** 2
