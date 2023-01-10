N, M = map(int, input().split())

graph = [i for i in range(101)]
for _ in range(N + M):
    x, y = map(int, input().split())
    graph[x] = y

pos = set([1])
count = 0
while 100 not in pos:
    count += 1
    pos = set(graph[v + i] for i in range(1, 7) for v in pos if v + i <= 100)
print(count)
