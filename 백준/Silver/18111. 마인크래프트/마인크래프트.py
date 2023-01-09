N, M, B = map(int, input().split())
G = []
for _ in range(N):
    G.extend(map(int, input().split()))
G_ = sorted(G)

minH = min(
    G_[min(int(N * M * 2 / 3), N * M - 1)],  # 2/3 Balance
    (B + sum(G)) // (N * M),  # Use every block
    256,  # Problem Condition
)
maxH = min(
    G_[min(int(N * M * 2 / 3), N * M - 1)] + 1,  # 2/3 Balance
    (B + sum(G)) // (N * M),  # Use every block
    256,  # Problem Condition
)

time = [sum(h - v if h > v else (v - h) * 2 for v in G) for h in range(minH, maxH + 1)]
v = min(enumerate(time), key=lambda o: (o[1], -o[0]))
print(v[1], v[0] + minH)
