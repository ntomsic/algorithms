"""
Given a non-empty string s and a dictionary wordDict
containing a list of non-empty words,
determine if s can be segmented into a space-separated
sequence of one or more dictionary words.
You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


# s = abc word_dict = ["a","bc"]
# True False False False


# TC: O(N^2)  SC: O(N)
def word_break(_s, word_dict):
    """
    :type _s: str
    :type word_dict: Set[str]
    :rtype: bool
    """
    d_p = [False] * (len(_s) + 1)
    d_p[0] = True
    for i in range(1, len(_s) + 1):
        for j in range(0, i):
            if d_p[j] and _s[j:i] in word_dict:
                d_p[i] = True
                break
    return d_p[-1]


if __name__ == "__main__":
    S = "keonkim"
    dic = ["keon", "kim"]

    print(word_break(S, dic))
