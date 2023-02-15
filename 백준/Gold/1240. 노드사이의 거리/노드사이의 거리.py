import sys

I = sys.stdin.readline
N, M = map(int, I().split())
L = [i for i in range(N + 1)]


def find(n):
    if L[n] != n:
        L[n] = find(L[n])
    return L[n]


def union(a, b):
    L[find(a)] = L[find(b)]


G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, D = map(int, I().split())
    ia, ib = find(A), find(B)
    sa, sb = set(), set()
    for i in range(1, N + 1):
        if find(i) == ia:
            sa.add(i)
        elif find(i) == ib:
            sb.add(i)
    for a in sa:
        for b in sb:
            if a == A and b == B:
                G[a][b], G[b][a] = D, D
            else:
                d = G[a][A] + D + G[B][b]
                G[a][b], G[b][a] = d, d
    union(A, B)
for _ in range(M):
    A, B = map(int, I().split())
    print(G[A][B])
