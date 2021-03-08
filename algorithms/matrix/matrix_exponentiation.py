def multiply(mat_a: list, mat_b: list) -> list:
    """
    Multiplies two square matrices matA and matB od size n x n
    Time Complexity: O(n^3)
    """
    _n = len(mat_a)
    mat_c = [[0 for i in range(_n)] for j in range(_n)]

    for i in range(_n):
        for j in range(_n):
            for k in range(_n):
                mat_c[i][j] += mat_a[i][k] * mat_b[k][j]

    return mat_c

def identity(_n: int) -> list:
    """
    Returns the Identity matrix of size n x n
    Time Complecity: O(n^2)
    """
    _i = [[0 for i in range(_n)] for j in range(_n)]

    for i in range(_n):
        _i[i][i] = 1

    return _i

def matrix_exponentiation(mat: list, _n: int) -> list:
    """
    Calculates mat^n by repeated squaring
    Time Complexity: O(d^3 log(n))
                     d: dimesion of the square matrix mat
                     n: power the matrix is raised to
    """
    if _n == 0:
        return identity(len(mat))
    if _n % 2 == 1:
        return multiply(matrix_exponentiation(mat, _n - 1), mat)
    tmp = matrix_exponentiation(mat, _n // 2)
    return multiply(tmp, tmp)
