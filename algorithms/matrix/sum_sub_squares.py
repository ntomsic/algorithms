# Function to find sum of all
# sub-squares of size k x k in a given
# square matrix of size n x n
def sum_sub_squares(matrix, k):
    _n = len(matrix)
    result = [[0 for i in range(k)] for j in range(k)]

    if k > _n:
        return
    for i in range(_n - k + 1):
        _l = 0
        for j in range(_n - k + 1):
            sum = 0

            # Calculate and print sum of current sub-square
            for _p in range(i, k + i):
                for _q in range(j, k + j):
                    sum += matrix[_p][_q]

            result[i][_l] = sum
            _l += 1

    return result
