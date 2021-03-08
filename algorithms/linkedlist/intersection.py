"""
   This function takes two lists and returns the node they have in common, if any.
   In this example:
   1 -> 3 -> 5
               \
                7 -> 9 -> 11
               /
   2 -> 4 -> 6
   ...we would return 7.
   Note that the node itself is the unique identifier, not the value of the node.
   """
import unittest


class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def intersection(h_1, h_2):
    count = 0
    flag = None
    h1_orig = h_1
    h2_orig = h_2

    while h_1 or h_2:
        count += 1

        if not flag and (h_1.next is None or h_2.next is None):
            # We hit the end of one of the lists, set a flag for this
            flag = (count, h_1.next, h_2.next)

        if h_1:
            h_1 = h_1.next
        if h_2:
            h_2 = h_2.next

    long_len = count  # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None:
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None:
        shorter = h2_orig
        longer = h1_orig

    while longer and shorter:

        while long_len > short_len:
            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1

        if longer == shorter:
            # The nodes match, return the node
            return longer
        else:
            longer = longer.next
            shorter = shorter.next

    return None


class TestSuite(unittest.TestCase):

    def test_intersection(self):
        # create linked list as:
        # 1 -> 3 -> 5
        #            \
        #             7 -> 9 -> 11
        #            /
        # 2 -> 4 -> 6
        a_1 = Node(1)
        b_1 = Node(3)
        c_1 = Node(5)
        _d = Node(7)
        a_2 = Node(2)
        b_2 = Node(4)
        c_2 = Node(6)
        _e = Node(9)
        _f = Node(11)

        a_1.next = b_1
        b_1.next = c_1
        c_1.next = _d
        a_2.next = b_2
        b_2.next = c_2
        c_2.next = _d
        _d.next = _e
        _e.next = _f

        self.assertEqual(7, intersection(a_1, a_2).val)


if __name__ == '__main__':
    unittest.main()
