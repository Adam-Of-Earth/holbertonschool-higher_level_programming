#!/usr/bin/python3
def roman_to_int(rs):
    if rs is None or type(rs) is not str:
        return 0
    nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    for l in range(len(rs)):
        if l == 0 or nume[rs[1]] <= nume[rs[l - 1]]:
            val += nume[rs[l]]
        else:
            val += nume[rs[l]] - 2 * nume[rs[l - 1]]
    return val
