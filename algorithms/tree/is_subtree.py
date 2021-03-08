"""
Given two binary trees s and t, check if t is a subtree of s.
A subtree of a tree t is a tree consisting of a node in t and
all of its descendants in t.

Example 1:

Given s:

     3
    / \
   4   5
  / \
 1   2

Given t:

   4
  / \
 1   2
Return true, because t is a subtree of s.

Example 2:

Given s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given t:

     3
    /
   4
  / \
 1   2
Return false, because even though t is part of s,
it does not contain all descendants of t.

Follow up:
What if one tree is significantly lager than the other?
"""
import collections


def is_subtree(big, small):
    flag = False
    queue = collections.deque()
    queue.append(big)
    while queue:
        node = queue.popleft()
        if node.val == small.val:
            flag = comp(node, small)
            break
        queue.append(node.left)
        queue.append(node.right)
    return flag


def comp(_p, _q):
    if _p is None and _q is None:
        return True
    if _p is not None and _q is not None:
        return _p.val == _q.val and comp(_p.left, _q.left) and comp(_p.right, _q.right)
    return False
