import heapq
import sys

I = sys.stdin.readline
L = [int(I()) for _ in range(int(I()))]
heapq.heapify(L)
counter = 0
for _ in range(len(L) - 1):
    c = heapq.heappop(L) + heapq.heappop(L)
    counter += c
    heapq.heappush(L, c)
print(counter)
