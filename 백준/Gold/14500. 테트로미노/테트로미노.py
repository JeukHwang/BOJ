N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
MAX = 0


def get(i, j):
    return MAP[i][j] if (0 <= i < N and 0 <= j < M) else 0


# XXX XXX XXX OXX XOX XXO
# OOO OOO OOO OOO OOO OOO OOOO
# OXX XOX XXO XXX XXX XXX
for i in range(N):
    for j in range(M - 2):
        middle = MAP[i][j] + MAP[i][j + 1] + MAP[i][j + 2]
        MAX = max(
            MAX,
            middle
            + max(
                get(i - 1, j),
                get(i - 1, j + 1),
                get(i - 1, j + 2),
                get(i + 1, j),
                get(i + 1, j + 1),
                get(i + 1, j + 2),
                get(i, j + 3),
            ),
        )

# OOX XOO OOX XOO
# OOX XOO XOO OOX
for i in range(N - 2):
    for j in range(M - 1):
        middle = MAP[i + 1][j] + MAP[i + 1][j + 1]
        MAX = max(
            MAX,
            middle
            + max(
                MAP[i][j] + MAP[i + 2][j + 1],
                MAP[i][j + 1] + MAP[i + 2][j],
                MAP[i][j] + MAP[i][j + 1],
                MAP[i + 2][j] + MAP[i + 2][j + 1],
            ),
        )

# reverse
for j in range(M):
    for i in range(N - 2):
        middle = MAP[i][j] + MAP[i + 1][j] + MAP[i + 2][j]
        MAX = max(
            MAX,
            middle
            + max(
                get(i, j - 1),
                get(i + 1, j - 1),
                get(i + 2, j - 1),
                get(i, j + 1),
                get(i + 1, j + 1),
                get(i + 2, j + 1),
                get(i + 3, j),
            ),
        )
for j in range(M - 2):
    for i in range(N - 1):
        middle = MAP[i][j + 1] + MAP[i + 1][j + 1]
        MAX = max(
            MAX,
            middle
            + max(
                MAP[i][j] + MAP[i + 1][j + 2],
                MAP[i][j + 2] + MAP[i + 1][j],
                MAP[i][j] + MAP[i + 1][j],
                MAP[i][j + 2] + MAP[i + 1][j + 2],
            ),
        )

print(MAX)
