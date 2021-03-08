"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""


def roman_to_int(_s: "str") -> "int":
    number = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(_s) - 1):
        if roman[_s[i]] < roman[_s[i + 1]]:
            number -= roman[_s[i]]
        else:
            number += roman[_s[i]]
    return number + roman[_s[-1]]


if __name__ == "__main__":
    ROMAN = "DCXXI"
    print(roman_to_int(ROMAN))
