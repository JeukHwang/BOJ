import sys

I = sys.stdin.readline
V, E = map(int, I().split())
queue = sorted([list(map(int, I().split())) for _ in range(E)], key=lambda x: -x[2])
L, value, partition = [i for i in range(V + 1)], 0, V


def get(n):
    if L[n] != n:
        m = get(L[n])
        L[n] = m
        return m
    else:
        return n


def union(n, m):
    L[get(m)] = get(n)


while partition > 1:
    a, b, c = queue.pop()
    if get(a) == get(b):
        continue
    union(a, b)
    partition -= 1
    value += c
print(value)
