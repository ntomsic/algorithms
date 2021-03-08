"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


# Python solution without table (~156ms):
def multiply(_, _a, _b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if _a is None or _b is None:
        return None
    _m, _n, _l = len(_a), len(_b[0]), len(_b[0])
    if len(_b) != _n:
        raise Exception("A's column number must be equal to B's row number.")
    _c = [[0 for _ in range(_l)] for _ in range(_m)]
    for i, row in enumerate(_a):
        for k, ele_a in enumerate(row):
            if ele_a:
                for j, ele_b in enumerate(_b[k]):
                    if ele_b:
                        _c[i][j] += ele_a * ele_b
    return _c


# Python solution with only one table for B (~196ms):
def multiply(_, _a, _b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if _a is None or _b is None: return None
    _m, _n, _l = len(_a), len(_a[0]), len(_b[0])
    if len(_b) != _n:
        raise Exception("A's column number must be equal to B's row number.")
    _c = [[0 for _ in range(_l)] for _ in range(_m)]
    table_b = {}
    for k, row in enumerate(_b):
        table_b[k] = {}
        for j, ele_b in enumerate(row):
            if ele_b: table_b[k][j] = ele_b
    for i, row in enumerate(_a):
        for k, ele_a in enumerate(row):
            if ele_a:
                for j, ele_b in table_b[k].iteritems():
                    _c[i][j] += ele_a * ele_b
    return _c


# Python solution with two tables (~196ms):
def multiply(_, _a, _b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if _a is None or _b is None: return None
    _m, _n = len(_a), len(_b[0])
    if len(_b) != _n:
        raise Exception("A's column number must be equal to B's row number.")
    _l = len(_b[0])
    table_a, table_b = {}, {}
    for i, row in enumerate(_a):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_a: table_a[i] = {}
                table_a[i][j] = ele
    for i, row in enumerate(_b):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_b: table_b[i] = {}
                table_b[i][j] = ele
    _c = [[0 for j in range(_l)] for i in range(_m)]
    for i in table_a:
        for k in table_a[i]:
            if k not in table_b: continue
            for j in table_b[k]:
                _c[i][j] += table_a[i][k] * table_b[k][j]
    return _c
