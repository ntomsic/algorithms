"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.
"""


def is_valid_sudoku(_, board):
    seen = []
    for i, row in enumerate(board):
        for j, _c in enumerate(row):
            if _c != '.':
                seen += [(_c, j), (i, _c), (i / 3, j / 3, _c)]
    return len(seen) == len(set(seen))
