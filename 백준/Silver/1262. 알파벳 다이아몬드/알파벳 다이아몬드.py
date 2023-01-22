n, r1, c1, r2, c2 = map(int, input().split())
grid, n1 = 2 * n - 1, n - 1


def diamond(x, y):
    diff = abs(x % grid - n1) + abs(y % grid - n1)
    return chr(diff % 26 + 97) if diff < n else "."


print(
    "\n".join(
        "".join(diamond(i, j) for j in range(c1, c2 + 1)) for i in range(r1, r2 + 1)
    )
)
