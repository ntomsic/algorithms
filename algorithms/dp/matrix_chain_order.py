'''
Dynamic Programming
Implementation of matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
'''
INF = float("inf")


def matrix_chain_order(array):
    _n = len(array)
    matrix = [[0 for x in range(_n)] for x in range(_n)]
    sol = [[0 for x in range(_n)] for x in range(_n)]
    for chain_length in range(2, _n):
        for _a in range(1, _n - chain_length + 1):
            _b = _a + chain_length - 1

            matrix[_a][_b] = INF
            for _c in range(_a, _b):
                cost = matrix[_a][_c] + matrix[_c + 1][_b] + array[_a - 1] * array[_c] * array[_b]
                if cost < matrix[_a][_b]:
                    matrix[_a][_b] = cost
                    sol[_a][_b] = _c
    return matrix, sol


# Print order of matrix with Ai as matrix

def print_optimal_solution(optimal_solution, i, j):
    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        print_optimal_solution(optimal_solution, i, optimal_solution[i][j])
        print_optimal_solution(optimal_solution, optimal_solution[i][j] + 1, j)
        print(")", end=" ")


def main():
    array = [30, 35, 15, 5, 10, 20, 25]
    _n = len(array)
    # Size of matrix created from above array will be
    # 30*35 35*15 15*5 5*10 10*20 20*25
    matrix, optimal_solution = matrix_chain_order(array)

    print("No. of Operation required: " + str((matrix[1][_n - 1])))
    print_optimal_solution(optimal_solution, 1, _n - 1)


if __name__ == '__main__':
    main()
