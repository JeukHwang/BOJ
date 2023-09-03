import sys

I = sys.stdin.readline
S, A, B, C = 0, 0, 0, 0
for i in range(int(I())):
    n = int(I())
    S, A, B, C = S + n, B, C, min(A, B, C) + n
print(S - min(A, B, C))
