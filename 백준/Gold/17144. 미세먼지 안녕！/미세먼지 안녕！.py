R, C, T = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(R)]

flag = False
for r in range(R):
    for c in range(C):
        if M[r][c] == -1:
            M[r][c] = 0
            M[r + 1][c] = 0
            pos = (r, c)
            flag = True
            break
    if flag:
        break
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def isPurifier(i, j):
    return pos == (i, j) or pos == (i - 1, j)


def adjacent(i, j):
    if isPurifier(i, j):
        return []
    return [
        (r + i, c + j)
        for (r, c) in direction
        if 0 <= r + i < R and 0 <= c + j < C and not isPurifier(r + i, c + j)
    ]


def wind(i, j):
    r, _ = pos
    if (i == 0 or i == R - 1) and j != 0:
        return i, j - 1
    if (i == r or i == r + 1) and j != C - 1:
        return i, j + 1
    if (i <= r and j == 0) or (i >= r + 1 and j == C - 1):
        return i + 1, j
    if (i <= r and j == C - 1) or (i >= r + 1 and j == 0):
        return i - 1, j
    return i, j


for _ in range(T):
    M_ = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            i_, j_ = wind(r, c)
            M_[i_][j_] = (
                sum((M[x][y] // 5 - M[r][c] // 5) for (x, y) in adjacent(r, c))
                + M[r][c]
            )
    x, y = pos
    M_[x][y] = 0
    M_[x + 1][y] = 0
    M = M_
print(sum(sum(v) for v in M))
