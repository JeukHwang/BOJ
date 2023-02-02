import sys

I = sys.stdin.readline
N, M = map(int, I().split())
smaller, larger = [0] * (N + 1), [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, I().split())
    larger[A].append(B)
    smaller[B] += 1

queue = [i for i in range(1, N + 1) if smaller[i] == 0]
while queue:
    i = queue.pop()
    for v in larger[i]:
        smaller[v] -= 1
        if smaller[v] == 0:
            queue.append(v)
    print(i, end=" ")
