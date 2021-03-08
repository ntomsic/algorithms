"""
Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x.  If x is contained
within the list, the values of x only need to be after the elements less than x.
The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.

3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

We assume the values of all linked list nodes are int and that x in an int.
"""


class Node():
    def __init__(self, val=None):
        self.val = int(val)
        self.next = None


def print_linked_list(head):
    string = ""
    while head.next:
        string += str(head.val) + " -> "
        head = head.next
    string += str(head.val)
    print(string)


def partition(head, _x):
    left = None
    right = None
    prev = None
    current = head
    while current:
        if int(current.val) >= _x:
            if not right:
                right = current
        else:
            if not left:
                left = current
            else:
                prev.next = current.next
                left.next = current
                left = current
                left.next = right
        if prev and prev.next is None:
            break
        # cache previous value in case it needs to be pointed elsewhere
        prev = current
        current = current.next


def test():
    _a = Node("3")
    _b = Node("5")
    _c = Node("8")
    _d = Node("5")
    _e = Node("10")
    _f = Node("2")
    _g = Node("1")

    _a.next = _b
    _b.next = _c
    _c.next = _d
    _d.next = _e
    _e.next = _f
    _f.next = _g

    print_linked_list(_a)
    partition(_a, 5)
    print_linked_list(_a)


if __name__ == '__main__':
    test()
