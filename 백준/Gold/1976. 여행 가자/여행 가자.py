import sys

I = sys.stdin.readline
N, M = int(I()), int(I())
S = [list(map(int, I().split())) for _ in range(N)]
E = [int(v) - 1 for v in I().split()]

L = [i for i in range(N)]


def get(n):
    if L[n] != n:
        L[n] = get(L[n])
    return L[n]


def union(n, m):
    L[get(m)] = get(n)


for i in range(N - 1):
    for j in range(i, N):
        if S[i][j] == 1:
            union(i, j)
print("YES" if all(get(e) == get(E[0]) for e in E) else "NO")
