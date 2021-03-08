"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generate_parenthesis_v1(_n):
    def add_pair(res, _s, left, right):
        if left == 0 and right == 0:
            res.append(_s)
            return
        if right > 0:
            add_pair(res, _s + ")", left, right - 1)
        if left > 0:
            add_pair(res, _s + "(", left - 1, right + 1)

    res = []
    add_pair(res, "", _n, 0)
    return res


def generate_parenthesis_v2(_n):
    def add_pair(res, _s, left, right):
        if left == 0 and right == 0:
            res.append(_s)
        if left > 0:
            add_pair(res, _s + "(", left - 1, right)
        if right > 0 and left < right:
            add_pair(res, _s + ")", left, right - 1)

    res = []
    add_pair(res, "", _n, _n)
    return res
