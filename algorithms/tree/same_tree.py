"""
Given two binary trees, write a function to check
if they are equal or not.

Two binary trees are considered equal if they are
structurally identical and the nodes have the same value.
"""


def is_same_tree(_p, _q):
    if _p is None and _q is None:
        return True
    if _p is not None and _q is not None and _p.val == _q.val:
        return is_same_tree(_p.left, _q.left) and is_same_tree(_p.right, _q.right)
    return False

# Time Complexity O(min(N,M))
# where N and M are the number of nodes for the trees.

# Space Complexity O(min(height1, height2))
# levels of recursion is the mininum height between the two trees.
