"""
Given string a and b, with b containing all distinct characters,
find the longest common sub sequence's length.

Expected complexity O(n logn).
"""


def max_common_sub_string(s_1, s_2):
    # Assuming s2 has all unique chars
    s2dic = {s_2[i]: i for i in range(len(s_2))}
    maxr = 0
    subs = ''
    i = 0
    while i < len(s_1):
        if s_1[i] in s2dic:
            j = s2dic[s_1[i]]
            k = i
            while j < len(s_2) and k < len(s_1) and s_1[k] == s_2[j]:
                k += 1
                j += 1
            if k - i > maxr:
                maxr = k - i
                subs = s_1[i:k]
            i = k
        else:
            i += 1
    return subs
