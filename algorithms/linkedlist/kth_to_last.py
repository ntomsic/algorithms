class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


def kth_to_last_eval(head, k):
    """
    This is a suboptimal, hacky method using eval(), which is not
     safe for user input. We guard against danger by ensuring k in an int
    """
    if not isinstance(k, int) or not head.val:
        return False

    nexts = '.'.join(['next' for n in range(1, k + 1)])
    seeker = str('.'.join(['head', nexts]))

    while head:
        if eval(seeker) is None:
            return head
        else:
            head = head.next

    return False


def kth_to_last_dict(head, k):
    """
    This is a brute force method where we keep a dict the size of the list
    Then we check it for the value we need. If the key is not in the dict,
    our and statement will short circuit and return False
    """
    if not (head and k > -1):
        return False
    _d = dict()
    count = 0
    while head:
        _d[count] = head
        head = head.next
        count += 1
    return len(_d) - k in _d and _d[len(_d) - k]


def kth_to_last(head, k):
    """
    This is an optimal method using iteration.
    We move p1 k steps ahead into the list.
    Then we move p1 and p2 together until p1 hits the end.
    """
    if not (head or k > -1):
        return False
    p_1 = head
    p_2 = head
    for _ in range(1, k + 1):
        if p_1 is None:
            # Went too far, k is not valid
            raise IndexError
        p_1 = p_1.next
    while p_1:
        p_1 = p_1.next
        p_2 = p_2.next
    return p_2


def print_linked_list(head):
    string = ""
    while head.next:
        string += head.val + " -> "
        head = head.next
    string += head.val
    print(string)


def test():
    # def make_test_li
    # A A B C D C F G
    a_1 = Node("A")
    a_2 = Node("A")
    _b = Node("B")
    c_1 = Node("C")
    _d = Node("D")
    c_2 = Node("C")
    _f = Node("F")
    _g = Node("G")
    a_1.next = a_2
    a_2.next = _b
    _b.next = c_1
    c_1.next = _d
    _d.next = c_2
    c_2.next = _f
    _f.next = _g
    print_linked_list(a_1)

    # test kth_to_last_eval
    kth = kth_to_last_eval(a_1, 4)
    try:
        assert kth.val == "D"
    except AssertionError as _e:
        _e.args += ("Expecting D, got %s" % kth.val,)
        raise

    # test kth_to_last_dict
    kth = kth_to_last_dict(a_1, 4)
    try:
        assert kth.val == "D"
    except AssertionError as _e:
        _e.args += ("Expecting D, got %s" % kth.val,)
        raise

    # test kth_to_last
    kth = kth_to_last(a_1, 4)
    try:
        assert kth.val == "D"
    except AssertionError as _e:
        _e.args += ("Expecting D, got %s" % kth.val,)
        raise
    print("all passed.")


if __name__ == '__main__':
    test()
