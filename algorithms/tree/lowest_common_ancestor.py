"""
Given a binary tree, find the lowest common ancestor
(LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes
    v and w as the lowest node in T that has both v and w as
    descendants
    (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.
"""


def lca(root, _p, _q):
    """
    :type root: TreeNode
    :type _p: TreeNode
    :type _q: TreeNode
    :rtype: TreeNode
    """
    if root is None or root is _p or root is _q:
        return root
    left = lca(root.left, _p, _q)
    right = lca(root.right, _p, _q)
    if left is not None and right is not None:
        return root
    return left if left else right
