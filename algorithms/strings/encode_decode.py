""" Design an algorithm to encode a list of strings to a string.
 The encoded mystring is then sent over the network and is decoded
 back to the original list of strings.
"""


# Implement the encode and decode methods.

def encode(strs):
    """Encodes a list of strings to a single string.
    :type strs: List[str]
    :rtype: str
    """
    res = ''
    for string in strs.split():
        res += str(len(string)) + ":" + string
    return res


def decode(_s):
    """Decodes a single string to a list of strings.
    :type _s: str
    :rtype: List[str]
    """
    strs = []
    i = 0
    while i < len(_s):
        index = _s.find(":", i)
        size = int(_s[i:index])
        strs.append(_s[index + 1: index + 1 + size])
        i = index + 1 + size
    return strs
