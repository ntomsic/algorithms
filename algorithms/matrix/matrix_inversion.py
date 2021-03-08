"""
Inverts an invertible n x n matrix -- i.e., given an n x n matrix A, returns
an n x n matrix B such that AB = BA = In, the n x n identity matrix.

For a 2 x 2 matrix, inversion is simple using the cofactor equation. For
larger matrices, this is a four step process:
1. calculate the matrix of minors: create an n x n matrix by considering each
position in the original matrix in turn. Exclude the current row and column
and calculate the determinant of the remaining matrix, then place that value
in the current position's equivalent in the matrix of minors.
2. create the matrix of cofactors: take the matrix of minors and multiply
alternate values by -1 in a checkerboard pattern.
3. adjugate: hold the top left to bottom right diagonal constant, but swap all
other values over it.
4. multiply the adjugated matrix by 1 / the determinant of the original matrix

This code combines steps 1 and 2 into one method to reduce traversals of the
matrix.

Possible edge cases: will not work for 0x0 or 1x1 matrix, though these are
trivial to calculate without use of this file.
"""
import fractions


def invert_matrix(_m):
    """invert an n x n matrix"""
    # Error conditions
    if not array_is_matrix(_m):
        print("Invalid matrix: array is not a matrix")
        return [[-1]]
    if len(_m) != len(_m[0]):
        print("Invalid matrix: matrix is not square")
        return [[-2]]
    if len(_m) < 2:
        print("Invalid matrix: matrix is too small")
        return [[-3]]
    if get_determinant(_m) == 0:
        print("Invalid matrix: matrix is square, but singular (determinant = 0)")
        return [[-4]]

    # Calculation
    if len(_m) == 2:
        # simple case
        multiplier = 1 / get_determinant(_m)
        inverted = [[multiplier] * len(_m) for n in range(len(_m))]
        inverted[0][1] = inverted[0][1] * -1 * _m[0][1]
        inverted[1][0] = inverted[1][0] * -1 * _m[1][0]
        inverted[0][0] = multiplier * _m[1][1]
        inverted[1][1] = multiplier * _m[0][0]
        return inverted
    # some steps combined in helpers to reduce traversals
    # get matrix of minors w/ "checkerboard" signs
    m_of_minors = get_matrix_of_minors(_m)

    # calculate determinant (we need to know 1/det)
    multiplier = fractions.Fraction(1, get_determinant(_m))

    # adjugate (swap on diagonals) and multiply by 1/det
    inverted = transpose_and_multiply(m_of_minors, multiplier)

    return inverted


def get_determinant(_m):
    """recursively calculate the determinant of an n x n matrix, n >= 2"""
    if len(_m) == 2:
        # trivial case
        return (_m[0][0] * _m[1][1]) - (_m[0][1] * _m[1][0])
    sign = 1
    det = 0
    for i in range(len(_m)):
        det += sign * _m[0][i] * get_determinant(get_minor(_m, 0, i))
        sign *= -1
    return det


def get_matrix_of_minors(_m):
    """get the matrix of minors and alternate signs"""
    matrix_of_minors = [[0 for i in range(len(_m))] for j in range(len(_m))]
    for row in range(len(_m)):
        for col in range(len(_m[0])):
            if (row + col) % 2 == 0:
                sign = 1
            else:
                sign = -1
            matrix_of_minors[row][col] = sign * get_determinant(get_minor(_m, row, col))
    return matrix_of_minors


def get_minor(_m, row, col):
    """
    get the minor of the matrix position m[row][col]
    (all values m[r][c] where r != row and c != col)
    """
    minors = []
    for i in range(len(_m)):
        if i != row:
            new_row = _m[i][:col]
            new_row.extend(_m[i][col + 1:])
            minors.append(new_row)
    return minors


def transpose_and_multiply(_m, multiplier=1):
    """swap values along diagonal, optionally adding multiplier"""
    for row in range(len(_m)):
        for col in range(row + 1):
            temp = _m[row][col] * multiplier
            _m[row][col] = _m[col][row] * multiplier
            _m[col][row] = temp
    return _m


def array_is_matrix(_m):
    if len(_m) == 0:
        return False
    first_col = len(_m[0])
    for row in _m:
        if len(row) != first_col:
            return False
    return True
