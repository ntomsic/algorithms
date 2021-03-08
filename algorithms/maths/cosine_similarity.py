"""
Calculate cosine similarity between given two 1d list.
Two list must have the same length.

Example:
cosine_similarity([1, 1, 1], [1, 2, -1])  # output : 0.47140452079103173
"""
import math


def _l2_distance(vec):
    """
    Calculate l2 distance from two given vectors.
    """
    norm = 0.
    for _e in vec:
        norm += _e * _e
    norm = math.sqrt(norm)
    return norm


def cosine_similarity(_a, _b):
    """
    Calculate cosine similarity between given two vectors
    :type _a: list
    :type _b: list
    """
    if len(_a) != len(_b):
        raise ValueError("The two vectors must be the same length. Got shape " + str(len(_a)) + " and " + str(len(_b)))

    norm_a = _l2_distance(_a)
    norm_b = _l2_distance(_b)

    similarity = 0.

    # Calculate the dot product of two vectors
    for a_e, b_e in zip(_a, _b):
        similarity += a_e * b_e

    similarity /= (norm_a * norm_b)

    return similarity
