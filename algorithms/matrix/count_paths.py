#
# Count the number of unique paths from a[0][0] to a[m-1][n-1]
# We are allowed to move either right or down from a cell in the matrix.
# Approaches-
# (i) Recursion- Recurse starting from a[m-1][n-1], upwards and leftwards,
#                add the path count of both recursions and return count.
# (ii) Dynamic Programming- Start from a[0][0].Store the count in a count
#                           matrix. Return count[m-1][n-1]
# T(n)- O(mn), S(n)- O(mn)
#


def count_paths(_m, _n):
    if _m < 1 or _n < 1:
        return -1
    count = [[None for j in range(_n)] for i in range(_m)]

    # Taking care of the edge cases- matrix of size 1xn or mx1
    for i in range(_n):
        count[0][i] = 1
    for j in range(_m):
        count[j][0] = 1

    for i in range(1, _m):
        for j in range(1, _n):
            # Number of ways to reach a[i][j] = number of ways to reach
            #                                   a[i-1][j] + a[i][j-1]
            count[i][j] = count[i - 1][j] + count[i][j - 1]

    print(count[_m - 1][_n - 1])


def main():
    _m, _n = map(int, input('Enter two positive integers: ').split())
    count_paths(_m, _n)


if __name__ == '__main__':
    main()
