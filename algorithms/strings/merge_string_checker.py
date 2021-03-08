"""
At a job interview, you are challenged to write an algorithm to check if a
given string, s, can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2 are in the same
order as in s. The interviewer gives you the following example and tells
you to figure out the rest from the given test cases.
'codewars' is a merge from 'cdw' and 'oears':
s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""


# Recursive Solution
def is_merge_recursive(_s, part1, part2):
    if not part1:
        return _s == part2
    if not part2:
        return _s == part1
    if not _s:
        return part1 + part2 == ''
    if _s[0] == part1[0] and is_merge_recursive(_s[1:], part1[1:], part2):
        return True
    if _s[0] == part2[0] and is_merge_recursive(_s[1:], part1, part2[1:]):
        return True
    return False


# An iterative approach
def is_merge_iterative(_s, part1, part2):
    tuple_list = [(_s, part1, part2)]
    while tuple_list:
        string, p_1, p_2 = tuple_list.pop()
        if string:
            if p_1 and string[0] == p_1[0]:
                tuple_list.append((string[1:], p_1[1:], p_2))
            if p_2 and string[0] == p_2[0]:
                tuple_list.append((string[1:], p_1, p_2[1:]))
        else:
            if not p_1 and not p_2:
                return True
    return False
