#!/usr/bin/python3
def roman_to_int(roman_string):
    dicti = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev, sum = 0, 0

    for c in roman_string:
        sum += dicti[c] if dicti[c] <= prev else dicti[c] - prev * 2
        prev = dicti[c]
    return sum
