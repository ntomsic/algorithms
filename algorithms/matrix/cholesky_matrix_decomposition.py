"""
Cholesky matrix decomposition is used to find the decomposition of a Hermitian positive-definite matrix A
into matrix V, so that V * V* = A, where V* denotes the conjugate transpose of L.
The dimensions of the matrix A must match.

This method is mainly used for numeric solution of linear equations Ax = b.

example:
Input matrix A:
[[  4,  12, -16],
 [ 12,  37, -43],
 [-16, -43,  98]]

Result:
[[2.0, 0.0, 0.0],
[6.0, 1.0, 0.0],
[-8.0, 5.0, 3.0]]

Time complexity of this algorithm is O(n^3), specifically about (n^3)/3

"""
import math


def cholesky_decomposition(_a):
    """
    :param _a: Hermitian positive-definite matrix of type List[List[float]]
    :return: matrix of type List[List[float]] if A can be decomposed, otherwise None
    """
    _n = len(_a)
    for a_i in _a:
        if len(a_i) != _n:
            return None
    _v = [[0.0] * _n for _ in range(_n)]
    for j in range(_n):
        sum_diagonal_element = 0
        for k in range(j):
            sum_diagonal_element = sum_diagonal_element + math.pow(_v[j][k], 2)
        sum_diagonal_element = _a[j][j] - sum_diagonal_element
        if sum_diagonal_element <= 0:
            return None
        _v[j][j] = math.pow(sum_diagonal_element, 0.5)
        for i in range(j+1, _n):
            sum_other_element = 0
            for k in range(j):
                sum_other_element += _v[i][k]*_v[j][k]
            _v[i][j] = (_a[i][j] - sum_other_element) / _v[j][j]
    return _v
