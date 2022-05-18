'''
Theatre Square in the capital city of Berland has a rectangular shape with
the size n×m meters. On the occasion of the city's anniversary,
a decision was taken to pave the Square with square granite flagstones.
Each flagstone is of the size a×a.
What is the least number of flagstones needed to pave the Square?
It's allowed to cover the surface larger than the Theatre Square,
but the Square has to be covered. It's not allowed to break the flagstones.
The sides of flagstones should be parallel to the sides of the Square.

Input
n=6, m=6, a=4    then output = 4
The input contains three positive integer numbers in the first line: n,m and a (1≤n,m,a≤109).

Output
Write the needed number of flagstones.
'''

import math


def getNumberOfFlagStones(n, m, a):
    h = 0
    w = 0
    if n / a <= 1:
        h = 1
    else:
        h = math.ceil(n / a)
    if m / a <= 1:
        w = 1
    else:
        w = math.ceil(m / a)
    return h * w


def main():
    test1 = getNumberOfFlagStones(3, 6, 4)
    test2 = getNumberOfFlagStones(6, 6, 4)
    print(test1)
    print(test2)


main()
