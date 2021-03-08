"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

For example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_list(l_1, l_2):
    ret = cur = Node(0)
    while l_1 and l_2:
        if l_1.val < l_2.val:
            cur.next = l_1
            l_1 = l_1.next
        else:
            cur.next = l_2
            l_2 = l_2.next
        cur = cur.next
    cur.next = l_1 or l_2
    return ret.next


# recursively
def merge_two_list_recur(l_1, l_2):
    if not l_1 or not l_2:
        return l_1 or l_2
    if l_1.val < l_2.val:
        l_1.next = merge_two_list_recur(l_1.next, l_2)
        return l_1
    l_2.next = merge_two_list_recur(l_1, l_2.next)
    return l_2
