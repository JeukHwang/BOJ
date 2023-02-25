import math
from fractions import Fraction
from functools import reduce

N = int(input())
L = [(i, Fraction(1, 1)) for i in range(N)]


def get_root(i):
    return L[i] if L[i][0] == i else get_root(L[i][0])


def calc(i):
    return L[i][1] * (Fraction(1, 1) if L[i][0] == i else calc(L[i][0]))


def union(i, j, pi, pj):
    L[get_root(j)[0]] = (i, Fraction(pj, pi) / calc(j))


for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    union(a, b, p, q)
G = [calc(i) for i in range(N)]
g = reduce(
    lambda acc, cur: acc * cur.denominator // math.gcd(acc, cur.denominator), G, 1
)
print(*[G[i] * Fraction(g, 1) for i in range(N)])
