import sys

I = sys.stdin.readline
N = int(I())
T, G = [-1] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    T[i], *G[i], _ = map(int, I().split())
t = [-1] * (N + 1)


def get(i):
    if t[i] == -1:
        t[i] = (max(get(n) for n in G[i]) if G[i] else 0) + T[i]
    return t[i]


print("\n".join(str(get(i)) for i in range(1, N + 1)))
