"""
Atbash cipher is mapping the alphabet to it's reverse.
So if we take "a" as it is the first letter, we change it to the last - z.

Example:
Attack at dawn --> Zggzxp zg wzdm

Complexity: O(n)
"""


def atbash(_s):
    translated = ""
    for i in range(len(_s)):
        _n = ord(_s[i])

        if _s[i].isalpha():

            if _s[i].isupper():
                _x = _n - ord('A')
                translated += chr(ord('Z') - _x)

            if _s[i].islower():
                _x = _n - ord('a')
                translated += chr(ord('z') - _x)
        else:
            translated += _s[i]
    return translated
