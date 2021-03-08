"""
Reverse a singly linked list. For example:

1 --> 2 --> 3 --> 4
After reverse:
4 --> 3 --> 2 --> 1
"""


#
# Iterative solution
# T(n)- O(n)
#
def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev


#
# Recursive solution
# T(n)- O(n)
#
def reverse_list_recursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    _p = head.next
    head.next = None
    revrest = reverse_list_recursive(_p)
    _p.next = head
    return revrest
