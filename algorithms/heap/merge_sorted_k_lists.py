"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

from heapq import heappop, heapreplace, heapify
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    dummy = node = ListNode(0)
    _h = [(n.val, n) for n in lists if n]
    heapify(_h)
    while _h:
        _, _n = _h[0]
        if _n.next is None:
            heappop(_h)  # only change heap size when necessary
        else:
            heapreplace(_h, (_n.next.val, _n.next))
        node.next = _n
        node = node.next

    return dummy.next


def merge_k_lists(lists):
    dummy = ListNode(None)
    curr = dummy
    _q = PriorityQueue()
    for node in lists:
        if node:
            _q.put((node.val, node))
    while not _q.empty():
        curr.next = _q.get()[1]  # These two lines seem to
        curr = curr.next  # be equivalent to :-   curr = q.get()[1]
        if curr.next:
            _q.put((curr.next.val, curr.next))
    return dummy.next


"""
I think my code's complexity is also O(nlogk) and not using heap or priority queue,
n means the total elements and k means the size of list.

The mergeTwoLists function in my code comes from the problem Merge Two Sorted Lists
whose complexity obviously is O(n), n is the sum of length of l1 and l2.

To put it simpler, assume the k is 2^x, So the progress of combination is like a full binary tree,
from bottom to top. So on every level of tree, the combination complexity is n,
because every level have all n numbers without repetition.
The level of tree is x, ie log k. So the complexity is O(n log k).

for example, 8 ListNode, and the length of every ListNode is x1, x2,
x3, x4, x5, x6, x7, x8, total is n.

on level 3: x1+x2, x3+x4, x5+x6, x7+x8 sum: n

on level 2: x1+x2+x3+x4, x5+x6+x7+x8 sum: n

on level 1: x1+x2+x3+x4+x5+x6+x7+x8 sum: n
"""
