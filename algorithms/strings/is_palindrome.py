"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.
For the purpose of this problem,
we define empty string as valid palindrome.
"""
from string import ascii_letters


def is_palindrome(_s):
    """
    :type _s: str
    :rtype: bool
    """
    i = 0
    j = len(_s) - 1
    while i < j:
        while not _s[i].isalnum():
            i += 1
        while not _s[j].isalnum():
            j -= 1
        if _s[i].lower() != _s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


"""
Here is a bunch of other variations of is_palindrome function.

Variation 1:
Find the reverse of the string and compare it with the original string

Variation 2:
Loop from the start to length/2 and check the first character and last character
and so on... for instance s[0] compared with s[n-1], s[1] == s[n-2]...

Variation 3:
Using stack idea. 

Note: We are assuming that we are just checking a one word string. To check if a complete sentence 
"""


def remove_punctuation(s):
    """
    Remove punctuation, case sensitivity and spaces
    """
    return "".join(i.lower() for i in s if i in ascii_letters)


# Variation 1
def string_reverse(_s):
    return _s[::-1]


def is_palindrome_reverse(_s):
    _s = remove_punctuation(_s)

    # can also get rid of the string_reverse function and just do this return s == s[::-1] in one line.
    if _s == string_reverse(_s):
        return True
    return False


# Variation 2
def is_palindrome_two_pointer(_s):
    _s = remove_punctuation(_s)

    for i in range(0, len(_s) // 2):
        if _s[i] != _s[len(_s) - i - 1]:
            return False
    return True


# Variation 3
def is_palindrome_stack(_s):
    stack = []
    _s = remove_punctuation(_s)

    for i in range(len(_s) // 2, len(_s)):
        stack.append(_s[i])
    for i in range(0, len(_s) // 2):
        if _s[i] != stack.pop():
            return False
    return True
