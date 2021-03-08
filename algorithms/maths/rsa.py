"""
RSA encryption algorithm
a method for encrypting a number that uses seperate encryption and decryption keys
this file only implements the key generation algorithm

there are three important numbers in RSA called n, e, and d
e is called the encryption exponent
d is called the decryption exponent
n is called the modulus

these three numbers satisfy
((x ** e) ** d) % n == x % n

to use this system for encryption, n and e are made publicly available, and d is kept secret
a number x can be encrypted by computing (x ** e) % n
the original number can then be recovered by computing (E ** d) % n, where E is
the encrypted number

fortunately, python provides a three argument version of pow() that can compute powers modulo
a number very quickly:
(a ** b) % c == pow(a,b,c)
"""

import random


def generate_key(k, seed=None):
    """
    the RSA key generating algorithm
    k is the number of bits in n
    """

    def modinv(_a, _m):
        """calculate the inverse of a mod m
        that is, find b such that (a * b) % m == 1"""
        _b = 1
        while not (_a * _b) % _m == 1:
            _b += 1
        return _b

    def gen_prime(k, seed=None):
        """generate a prime with k bits"""

        def is_prime(num):
            if num == 2:
                return True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        random.seed(seed)
        while True:
            key = random.randrange(int(2 ** (k - 1)), int(2 ** k))
            if is_prime(key):
                return key

    # size in bits of p and q need to add up to the size of n
    p_size = k / 2
    q_size = k - p_size

    _e = gen_prime(k, seed)  # in many cases, e is also chosen to be a small constant

    while True:
        _p = gen_prime(p_size, seed)
        if _p % _e != 1:
            break

    while True:
        _q = gen_prime(q_size, seed)
        if _q % _e != 1:
            break

    _n = _p * _q
    _l = (_p - 1) * (_q - 1)  # calculate totient function
    _d = modinv(_e, _l)

    return int(_n), int(_e), int(_d)


def encrypt(data, _e, _n):
    return pow(int(data), int(_e), int(_n))


def decrypt(data, _d, _n):
    return pow(int(data), int(_d), int(_n))

# sample usage:
# n,e,d = generate_key(16)
# data = 20
# encrypted = pow(data,e,n)
# decrypted = pow(encrypted,d,n)
# assert decrypted == data
