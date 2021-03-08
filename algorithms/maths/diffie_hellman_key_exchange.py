import math
from random import randint

"""
Code from /algorithms/maths/prime_check.py,
written by 'goswami-rahul' and 'Hai Honag Dang'
"""


def prime_check(_n):
    """Return True if n is a prime number
    Else return False.
    """

    if _n <= 1:
        return False
    if _n in (2, 3):
        return True
    if _n % 2 == 0 or _n % 3 == 0:
        return False
    j = 5
    while j * j <= _n:
        if _n % j == 0 or _n % (j + 2) == 0:
            return False
        j += 6
    return True


def find_order(_a, _n):
    """
    For positive integer n and given integer a that satisfies gcd(a, n) = 1,
    the order of a modulo n is the smallest positive integer k that satisfies
    pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).
    Order of certain number may or may not be exist. If so, return -1.
    """
    if (_a == 1) & (_n == 1):
        return 1
        # Exception Handling : 1 is the order of of 1
    if math.gcd(_a, _n) != 1:
        print("a and n should be relative prime!")
        return -1
    for i in range(1, _n):
        if pow(_a, i) % _n == 1:
            return i
    return -1


def euler_totient(_n):
    """
    Euler's totient function, also known as phi-function ϕ(n),
    counts the number of integers between 1 and n inclusive,
    which are coprime to n.
    (Two numbers are coprime if their greatest common divisor (GCD) equals 1).
    Code from /algorithms/maths/euler_totient.py, written by 'goswami-rahul'
    Time Complexity: O(sqrt(n)).
    """
    result = _n
    for i in range(2, int(_n ** 0.5) + 1):
        if _n % i == 0:
            while _n % i == 0:
                _n //= i
            result -= result // i
    if _n > 1:
        result -= result // _n
    return result


def find_primitive_root(_n):
    """
    For positive integer n and given integer a that satisfies gcd(a, n) = 1,
    a is the primitive root of n, if a's order k for n satisfies k = ϕ(n).
    Primitive roots of certain number may or may not be exist.
    If so, return empty list.
    """
    if _n == 1:
        return [0]
        # Exception Handling: 0 is the only primitive root of 1
    phi = euler_totient(_n)
    p_root_list = []
    # It will return every primitive roots of n.
    for i in range(1, _n):
        if math.gcd(i, _n) != 1:
            continue
            # To have order, a and n must be relative prime with each other.
        order = find_order(i, _n)
        if order == phi:
            p_root_list.append(i)
        continue
    return p_root_list


"""
Diffie-Hellman key exchange is the method that enables
two entities (in here, Alice and Bob), not knowing each other,
to share common secret key through not-encrypted communication network.
This method use the property of one-way function (discrete logarithm)
For example, given a, b and n, it is easy to calculate x
that satisfies (a^b) ≡ x (mod n).
However, it is very hard to calculate x that satisfies (a^x) ≡ b (mod n).
For using this method, large prime number p and its primitive root a must be given.
"""


def alice_private_key(_p):
    """Alice determine her private key
    in the range of 1 ~ p-1.
    This must be kept in secret"""
    return randint(1, _p - 1)


def alice_public_key(a_pr_k, _a, _p):
    """Alice calculate her public key
    with her private key.
    This is open to public"""
    return pow(_a, a_pr_k) % _p


def bob_private_key(_p):
    """Bob determine his private key
    in the range of 1 ~ p-1.
    This must be kept in secret"""
    return randint(1, _p - 1)


def bob_public_key(b_pr_k, _a, _p):
    """Bob calculate his public key
    with his private key.
    This is open to public"""
    return pow(_a, b_pr_k) % _p


def alice_shared_key(b_pu_k, a_pr_k, _p):
    """ Alice calculate secret key shared with Bob,
    with her private key and Bob's public key.
    This must be kept in secret"""
    return pow(b_pu_k, a_pr_k) % _p


def bob_shared_key(a_pu_k, b_pr_k, _p):
    """ Bob calculate secret key shared with Alice,
    with his private key and Alice's public key.
    This must be kept in secret"""
    return pow(a_pu_k, b_pr_k) % _p


def diffie_hellman_key_exchange(_a, _p, option=None):
    if option is not None:
        option = 1
        # Print explanation of process
        # when option parameter is given
    if not prime_check(_p):
        print("%d is not a prime number" % _p)
        return False
        # p must be large prime number
    try:
        p_root_list = find_primitive_root(_p)
        p_root_list.index(_a)
    except ValueError:
        print("%d is not a primitive root of %d" % (_a, _p))
        return False
        # a must be primitive root of p

    a_pr_k = alice_private_key(_p)
    a_pu_k = alice_public_key(a_pr_k, _a, _p)

    b_pr_k = bob_private_key(_p)
    b_pu_k = bob_public_key(b_pr_k, _a, _p)

    if option == 1:
        print("Private key of Alice = %d" % a_pr_k)
        print("Public key of Alice = %d" % a_pu_k)
        print("Private key of Bob = %d" % b_pr_k)
        print("Public key of Bob = %d" % b_pu_k)

    # In here, Alice send her public key to Bob, and Bob also send his public key to Alice.

    a_sh_k = alice_shared_key(b_pu_k, a_pr_k, _p)
    b_sh_k = bob_shared_key(a_pu_k, b_pr_k, _p)
    print("Shared key calculated by Alice = %d" % a_sh_k)
    print("Shared key calculated by Bob = %d" % b_sh_k)

    return a_sh_k == b_sh_k
