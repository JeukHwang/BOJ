def spiral(x, y):
    n = max(abs(x), abs(y))
    dist = abs(x - n) + abs(y - n)
    # return (2 * n - 1) ** 2 + (dist if y > x else (8 * n - dist))
    return ((2 * n - 1) ** 2 + dist) if y > x else ((2 * n + 1) ** 2 - dist)


r1, c1, r2, c2 = map(int, input().split())
l = len(str(max(spiral(r1, c1), spiral(r1, c2), spiral(r2, c1), spiral(r2, c2))))
print(
    "\n".join(
        " ".join(f"%{l}d" % spiral(i, j) for j in range(c1, c2 + 1))
        for i in range(r1, r2 + 1)
    )
)
