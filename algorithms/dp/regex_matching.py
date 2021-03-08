"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool is_match(const char *s, const char *p)

Some examples:
is_match("aa","a") → false
is_match("aa","aa") → true
is_match("aaa","aa") → false
is_match("aa", "a*") → true
is_match("aa", ".*") → true
is_match("ab", ".*") → true
is_match("aab", "c*a*b") → true
"""
import unittest


class Solution(object):
    def is_match(self, _s, _p):
        _m, _n = len(_s) + 1, len(_p) + 1
        matches = [[False] * _n for _ in range(_m)]

        # Match empty string with empty pattern
        matches[0][0] = True

        # Match empty string with .*
        for i, element in enumerate(_p[1:], 2):
            matches[0][i] = matches[0][i - 2] and element == '*'

        for i, s_s in enumerate(_s, 1):
            for j, p_p in enumerate(_p, 1):
                if p_p != '*':
                    # The previous character has matched and the current one
                    # has to be matched. Two possible matches: the same or .
                    matches[i][j] = matches[i - 1][j - 1] and \
                                    (s_s == p_p or p_p == '.')
                else:
                    # Horizontal look up [j - 2].
                    # Not use the character before *.
                    matches[i][j] |= matches[i][j - 2]

                    # Vertical look up [i - 1].
                    # Use at least one character before *.
                    #   p a b *
                    # s 1 0 0 0
                    # a 0 1 0 1
                    # b 0 0 1 1
                    # b 0 0 0 ?
                    if s_s == _p[j - 2] or _p[j - 2] == '.':
                        matches[i][j] |= matches[i - 1][j]

        return matches[-1][-1]


class TestSolution(unittest.TestCase):
    def test_none_0(self):
        _s = ""
        _p = ""
        self.assertTrue(Solution().is_match(_s, _p))

    def test_none_1(self):
        _s = ""
        _p = "a"
        self.assertFalse(Solution().is_match(_s, _p))

    def test_no_symbol_equal(self):
        _s = "abcd"
        _p = "abcd"
        self.assertTrue(Solution().is_match(_s, _p))

    def test_no_symbol_not_equal_0(self):
        _s = "abcd"
        _p = "efgh"
        self.assertFalse(Solution().is_match(_s, _p))

    def test_no_symbol_not_equal_1(self):
        _s = "ab"
        _p = "abb"
        self.assertFalse(Solution().is_match(_s, _p))

    def test_symbol_0(self):
        _s = ""
        _p = "a*"
        self.assertTrue(Solution().is_match(_s, _p))

    def test_symbol_1(self):
        _s = "a"
        _p = "ab*"
        self.assertTrue(Solution().is_match(_s, _p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        _s = "abb"
        _p = "ab*"
        self.assertTrue(Solution().is_match(_s, _p))


if __name__ == "__main__":
    unittest.main()
