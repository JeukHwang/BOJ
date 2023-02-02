import sys

I = sys.stdin.readline
N = int(I())
G = [None] * (N + 1)
for i in range(1, N + 1):
    t, *ns, _ = map(int, I().split())
    G[i] = (t, ns)
T = [-1] * (N + 1)


def get(i):
    if T[i] == -1:
        t, ns = G[i]
        T[i] = (max(get(n) for n in ns) if ns else 0) + t
    return T[i]


print("\n".join(str(get(i)) for i in range(1, N + 1)))
