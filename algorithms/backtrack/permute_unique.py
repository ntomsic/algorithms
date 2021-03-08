"""
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permute_unique(nums):
    perms = [[]]
    for _n in nums:
        new_perms = []
        for _l in perms:
            for i in range(len(_l) + 1):
                new_perms.append(_l[:i] + [_n] + _l[i:])
                if i < len(_l) and _l[i] == _n:
                    break  # handles duplication
        perms = new_perms
    return perms
