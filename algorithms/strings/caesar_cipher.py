"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you
past the end of the alphabet, just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""


def caesar_cipher(_s, k):
    result = ""
    for char in _s:
        _n = ord(char)
        if 64 < _n < 91:
            _n = ((_n - 65 + k) % 26) + 65
        if 96 < _n < 123:
            _n = ((_n - 97 + k) % 26) + 97
        result = result + chr(_n)
    return result
