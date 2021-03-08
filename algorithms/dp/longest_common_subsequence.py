"""
A subsequence is a sequence that can be derived from another
sequence by deleting some or no elements without changing the
order of the remaining elements.

For example, 'abd' is a subsequence of 'abcd' whereas 'adc' is not

Given 2 strings containing lowercase english alphabets, find the length
of the Longest Common Subsequence (L.C.S.).

Example:
    Input:  'abcdgh'
            'aedfhr'
    Output: 3

    Explanation: The longest subsequence common to both the string is "adh"

Time Complexity : O(M*N)
Space Complexity : O(M*N), where M and N are the lengths of the 1st and 2nd string
respectively.

"""


def longest_common_subsequence(s_1, s_2):
    """
    :param s_1: string
    :param s_2: string
    :return: int
    """
    _m = len(s_1)
    _n = len(s_2)

    d_p = [[0] * (_n + 1) for i in range(_m + 1)]
    """
    dp[i][j] : contains length of LCS of s1[0..i-1] and s2[0..j-1]
    """

    for i in range(_m + 1):
        for j in range(_n + 1):
            if i == 0 or j == 0:
                d_p[i][j] = 0
            elif s_1[i - 1] == s_2[j - 1]:
                d_p[i][j] = d_p[i - 1][j - 1] + 1
            else:
                d_p[i][j] = max(d_p[i - 1][j], d_p[i][j - 1])

    return d_p[_m][_n]
