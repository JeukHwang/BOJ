from itertools import combinations

L, C = map(int, input().split())
A = sorted(input().split())
V = set("aeiou")
for combination in combinations(A, L):
    if 1 <= len(V.intersection(combination)) <= L - 2:
        print("".join(combination))
