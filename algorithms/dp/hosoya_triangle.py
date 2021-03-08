"""
Hosoya triangle (originally Fibonacci triangle) is a triangular arrangement
of numbers, where if you take any number it is the sum of 2 numbers above.
First line is always 1, and second line is always {1     1}.

This printHosoya function takes argument n which is the height of the triangle
(number of lines).

For example:
printHosoya( 6 ) would return:
1
1 1
2 1 2
3 2 2 3
5 3 4 3 5
8 5 6 6 5 8

The complexity is O(n^3).

"""


def hosoya(_n, _m):
    if ((_n == 0 and _m == 0) or (_n == 1 and _m == 0) or
            (_n == 1 and _m == 1) or (_n == 2 and _m == 1)):
        return 1
    if _n > _m:
        return hosoya(_n - 1, _m) + hosoya(_n - 2, _m)
    if _m == _n:
        return hosoya(_n - 1, _m - 1) + hosoya(_n - 2, _m - 2)
    return 0


def print_hosoya(_n):
    for i in range(_n):
        for j in range(i + 1):
            print(hosoya(i, j), end=" ")
        print("\n", end="")


def hosoya_testing(_n):
    _x = []
    for i in range(_n):
        for j in range(i + 1):
            _x.append(hosoya(i, j))
    return _x
