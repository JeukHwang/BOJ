N = int(input())
L = [int(input()) for _ in range(N)]

A, B, C = 0, 0, 0
for i in range(N):
    A, B, C = B, C, min(A, B, C) + L[i]
print(sum(L) - min(A, B, C))
