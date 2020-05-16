# OLD_RESEARCH

Very Old Research For Historical Purposes

Very Old Work on Riverian Family Functions (LoL XD)
This is a Riverian Function is a number that in their digits contains the sums of each subset on the list
The original idea was that to search for a specific target you only had to look at the output of the function.
It is theoretically interesting and is one of the beginnings of the NUMBER THEORY EQUATION OF SAT (http://independent.academia.edu/oarr) but is not practical.


    # python3 ssp_riverian_family_functions.py
    1113010820055900528005900055900036000050110801077005540052300585005540003100000
    0 []
    31 [31]
    554 [554]
    585 [31, 554]
    523 [523]
    554 [31, 523]
    1077 [554, 523]
    1108 [31, 554, 523]
    5 [5]
    36 [31, 5]
    559 [554, 5]
    590 [31, 554, 5]
    528 [523, 5]
    559 [31, 523, 5]
    1082 [554, 523, 5]
    1113 [31, 554, 523, 5]

First H Familly Function from https://github.com/www-PEQNP-science/OLD_RESEARCH/blob/master/P_NP_The_Collapse_of_Hierarchies.pdf

def h(n):
    return (2 ** n) ** (2 ** n) + ((2 ** n) - (2 ** n) ** (2 ** n)) // (2 ** n - 1) ** 2


if __name__ == '__main__':
    print(bin(h(1))[2:])
    print(bin(h(2))[2:])
    print(bin(h(3))[2:])
    print(bin(h(4))[2:])

"""
10
11100100
111110101100011010001000
1111111011011100101110101001100001110110010101000011001000010000
"""
