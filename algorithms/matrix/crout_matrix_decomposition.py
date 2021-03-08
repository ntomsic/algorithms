"""
Crout matrix decomposition is used to find two matrices that, when multiplied
give our input matrix, so L * U = A.
L stands for lower and L has non-zero elements only on diagonal and below.
U stands for upper and U has non-zero elements only on diagonal and above.

This can for example be used to solve systems of linear equations.
The last if is used  if  to avoid dividing by zero.

Example:
We input the A matrix:
[[1,2,3],
[3,4,5],
[6,7,8]]

We get:
L = [1.0,  0.0, 0.0]
    [3.0, -2.0, 0.0]
    [6.0, -5.0, 0.0]
U = [1.0,  2.0, 3.0]
    [0.0,  1.0, 2.0]
    [0.0,  0.0, 1.0]

We can check that L * U = A.

I think the complexity should be O(n^3).
"""

def crout_matrix_decomposition(_a):
    _n = len(_a)
    _l = [[0.0] * _n for i in range(_n)]
    _u = [[0.0] * _n for i in range(_n)]
    for j in range(_n):
        _u[j][j] = 1.0
        for i in range(j, _n):
            alpha = float(_a[i][j])
            for k in range(j):
                alpha -= _l[i][k] * _u[k][j]
            _l[i][j] = float(alpha)
        for i in range(j + 1, _n):
            temp_u = float(_a[j][i])
            for k in range(j):
                temp_u -= float(_l[j][k] * _u[k][i])
            if int(_l[j][j]) == 0:
                _l[j][j] = float(0.1 ** 40)
            _u[j][i] = float(temp_u / _l[j][j])
    return _l, _u
