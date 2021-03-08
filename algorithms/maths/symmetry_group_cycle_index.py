from fractions import Fraction
from typing import Dict, Union

from gcd import lcm
from polynomial import (Monomial, Polynomial)

"""
	The significance of the cycle index (polynomial) of symmetry group
	is deeply rooted in counting the number of configurations
	of an object excluding those that are symmetric (in terms of permutations).

	For example, the following problem can be solved as a direct
	application of the cycle index polynomial of the symmetry
	group.

	Note: I came across this problem as a Google's foo.bar challenge at Level 5
	and solved it using a purely Group Theoretic approach. :)

	-----

	Problem:

	Given positive integers
	w, h, and s,
	compute the number of distinct 2D
	grids of dimensions w x h that contain
	entries from {0, 1, ..., s-1}.
	Note that two grids are defined
	to be equivalent if one can be
	obtained from the other by
	switching rows and columns
	some number of times.

	-----

	Approach:

	Compute the cycle index (polynomials)
	of S_w, and S_h, i.e. the Symmetry
	group on w and h symbols respectively.

	Compute the product of the two
	cycle indices while combining two
	monomials in such a way that
	for any pair of cycles c1, and c2
	in the elements of S_w X S_h,
	the resultant monomial contains
	terms of the form:
	$$ x_{lcm(|c1|, |c2|)}^{gcd(|c1|, |c2|)} $$

	Return the specialization of
	the product of cycle indices
	at x_i = s (for all the valid i).

	-----

	Code:

	def solve(w, h, s):

		s1 = get_cycle_index_sym(w)
	    s2 = get_cycle_index_sym(h)

	    result = cycle_product_for_two_polynomials(s1, s2, s)

	    return str(result)

"""


def cycle_product(m_1: Monomial, m_2: Monomial) -> Monomial:
    """
    Given two monomials (from the
    cycle index of a symmetry group),
    compute the resultant monomial
    in the cartesian product
    corresponding to their merging.
    """
    assert isinstance(m_1, Monomial) and isinstance(m_2, Monomial)
    _a = m_1.variables
    _b = m_2.variables
    result_variables = dict()
    for i in _a:
        for j in _b:
            k = lcm(i, j)
            _g = (i * j) // k
            if k in result_variables:
                result_variables[k] += _a[i] * _b[j] * _g
            else:
                result_variables[k] = _a[i] * _b[j] * _g

    return Monomial(result_variables, Fraction(m_1.coeff * m_2.coeff, 1))


def cycle_product_for_two_polynomials(p_1: Polynomial, p_2: Polynomial, _q: Union[float, int, Fraction]) -> Union[
    float, int, Fraction]:
    """
    Compute the product of
    given cycle indices p1,
    and p2 and evaluate it at q.
    """
    ans = Fraction(0, 1)
    for m_1 in p_1.monomials:
        for m_2 in p_2.monomials:
            ans += cycle_product(m_1, m_2).substitute(_q)

    return ans


def cycle_index_sym_helper(_n: int, memo: Dict[int, Polynomial]) -> Polynomial:
    """
    A helper for the dp-style evaluation
    of the cycle index.

    The recurrence is given in:
    https://en.wikipedia.org/wiki/Cycle_index#Symmetric_group_Sn

    """
    if _n in memo:
        return memo[_n]
    ans = Polynomial([Monomial({}, Fraction(0, 1))])
    for _t in range(1, _n + 1):
        ans = ans.__add__(Polynomial([Monomial({_t: 1}, Fraction(1, 1))]) * cycle_index_sym_helper(_n - _t, memo))
    ans *= Fraction(1, _n)
    memo[_n] = ans
    return memo[_n]


def get_cycle_index_sym(_n: int) -> Polynomial:
    """
    Compute the cycle index
    of S_n, i.e. the symmetry
    group of n symbols.

    """
    if _n < 0:
        raise ValueError('n should be a non-negative integer.')

    memo = {
        0: Polynomial([
            Monomial({}, Fraction(1, 1))
        ]),
        1: Polynomial([
            Monomial({1: 1}, Fraction(1, 1))
        ]),
        2: Polynomial([
            Monomial({1: 2}, Fraction(1, 2)),
            Monomial({2: 1}, Fraction(1, 2))
        ]),
        3: Polynomial([
            Monomial({1: 3}, Fraction(1, 6)),
            Monomial({1: 1, 2: 1}, Fraction(1, 2)),
            Monomial({3: 1}, Fraction(1, 3))
        ]),
        4: Polynomial([
            Monomial({1: 4}, Fraction(1, 24)),
            Monomial({2: 1, 1: 2}, Fraction(1, 4)),
            Monomial({3: 1, 1: 1}, Fraction(1, 3)),
            Monomial({2: 2}, Fraction(1, 8)),
            Monomial({4: 1}, Fraction(1, 4)),
        ])
    }
    result = cycle_index_sym_helper(_n, memo)
    return result
