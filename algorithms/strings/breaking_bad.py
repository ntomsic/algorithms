import re
from functools import reduce
"""
Given an api which returns an array of words and an array of symbols, display
the word with their matched symbol surrounded by square brackets.

If the word string matches more than one symbol, then choose the one with
longest length. (ex. 'Microsoft' matches 'i' and 'cro'):

Example:
Words array: ['Amazon', 'Microsoft', 'Google']
Symbols: ['i', 'Am', 'cro', 'Na', 'le', 'abc']

Output:
[Am]azon, Mi[cro]soft, Goog[le]

My solution(Wrong):
(I sorted the symbols array in descending order of length and ran loop over
words array to find a symbol match(using indexOf in javascript) which
worked. But I didn't make it through the interview, I am guessing my solution
was O(n^2) and they expected an efficient algorithm.

output:
['[Am]azon', 'Mi[cro]soft', 'Goog[le]', 'Amaz[o]n', 'Micr[o]s[o]ft', 'G[o][o]gle']
"""


def match_symbol(words, symbols):
    combined = []
    for _s in symbols:
        for _c in words:
            _r = re.search(_s, _c)
            if _r:
                combined.append(re.sub(_s, "[{}]".format(_s), _c))
    return combined


def match_symbol_1(words, symbols):
    res = []
    # reversely sort the symbols according to their lengths.
    symbols = sorted(symbols, key=lambda _: len(_), reverse=True)
    for word in words:
        for symbol in symbols:
            word_replaced = ''
            # once match, append the `word_replaced` to res, process next word
            if word.find(symbol) != -1:
                word_replaced = word.replace(symbol, '[' + symbol + ']')
                res.append(word_replaced)
                break
        # if this word matches no symbol, append it.
        if word_replaced == '':
            res.append(word)
    return res


class TreeNode:
    def __init__(self):
        self.c = dict()
        self.sym = None


def bracket(words, symbols):
    """
    Another approach is to use a Tree for the dictionary (the symbols), and then
    match brute force. The complexity will depend on the dictionary;
    if all are suffixes of the other, it will be n*m
    (where m is the size of the dictionary). For example, in Python:
    """
    root = TreeNode()
    for _s in symbols:
        _t = root
        for char in _s:
            if char not in _t.c:
                _t.c[char] = TreeNode()
            _t = _t.c[char]
        _t.sym = _s
    result = dict()
    for word in words:
        i = 0
        symlist = list()
        while i < len(word):
            j, _t = i, root
            while j < len(word) and word[j] in _t.c:
                _t = _t.c[word[j]]
                if _t.sym is not None:
                    symlist.append((j + 1 - len(_t.sym), j + 1, _t.sym))
                j += 1
            i += 1
        if len(symlist) > 0:
            sym = reduce(lambda x, y: x if x[1] - x[0] >= y[1] - y[0] else y,
                         symlist)
            result[word] = "{}[{}]{}".format(word[:sym[0]], sym[2],
                                             word[sym[1]:])
    return tuple(word if word not in result else result[word] for word in words)
