from math import comb

N, K = map(int, input().split())
print(comb(N + K - 1, N) % (10**9))
