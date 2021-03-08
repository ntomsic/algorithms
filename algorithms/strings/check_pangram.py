"""
Algorithm that checks if a given string is a pangram or not
"""


def check_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_string.lower():
            return False
    return True
