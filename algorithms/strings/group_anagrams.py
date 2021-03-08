"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


def group_anagrams(strs):
    _d = {}
    ans = []
    k = 0
    for str in strs:
        sstr = ''.join(sorted(str))
        if sstr not in _d:
            _d[sstr] = k
            k += 1
            ans.append([])
            ans[-1].append(str)
        else:
            ans[_d[sstr]].append(str)
    return ans
