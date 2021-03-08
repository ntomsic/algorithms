def reverse_vowel(_s):
    vowels = "AEIOUaeiou"
    i, j = 0, len(_s) - 1
    _s = list(_s)
    while i < j:
        while i < j and _s[i] not in vowels:
            i += 1
        while i < j and _s[j] not in vowels:
            j -= 1
        _s[i], _s[j] = _s[j], _s[i]
        i, j = i + 1, j - 1
    return "".join(_s)
