def recursive(_s):
    _l = len(_s)
    if _l < 2:
        return _s
    return recursive(_s[_l // 2:]) + recursive(_s[:_l // 2])


def iterative(_s):
    _r = list(_s)
    i, j = 0, len(_s) - 1
    while i < j:
        _r[i], _r[j] = _r[j], _r[i]
        i += 1
        j -= 1
    return "".join(_r)


def pythonic(_s):
    _r = list(reversed(_s))
    return "".join(_r)


def ultra_pythonic(_s):
    return _s[::-1]
