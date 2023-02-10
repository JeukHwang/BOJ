import heapq
import sys

I = sys.stdin.readline
L = [int(I()) for _ in range(int(I()))]
heapq.heapify(L)
counter = 0
while len(L) > 1:
    a, b = heapq.heappop(L), heapq.heappop(L)
    heapq.heappush(L, a + b)
    counter += a + b
print(counter)
