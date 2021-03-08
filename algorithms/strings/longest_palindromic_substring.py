'''
Given string s, find the longest palindromic substring.

Example1:

* input: "dasdasdasdasdasdadsa"
* output: "asdadsa"

Example2:

* input: "acdbbdaa"
* output: "dbbd"

Manacher's algorithm

'''


def longest_palindrome(_s):
    if len(_s) < 2:
        return _s

    n_str = '#' + '#'.join(_s) + '#'
    _p = [0] * len(n_str)
    m_x, loc = 0, 0
    index, maxlen = 0, 0
    for i in range(len(n_str)):
        if i < m_x and 2 * loc - i < len(n_str):
            _p[i] = min(m_x - i, _p[2 * loc - i])
        else:
            _p[i] = 1

        while _p[i] + i < len(n_str) and i - _p[i] >= 0 and n_str[
            i - _p[i]] == n_str[i + _p[i]]:
            _p[i] += 1

        if i + _p[i] > m_x:
            m_x = i + _p[i]
            loc = i

        if _p[i] > maxlen:
            index = i
            maxlen = _p[i]
    _s = n_str[index - _p[index] + 1:index + _p[index]]
    return _s.replace('#', '')
