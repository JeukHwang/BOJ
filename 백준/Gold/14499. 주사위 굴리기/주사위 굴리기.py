N, M, x, y, K = map(int, input().split())
L = [[int(v) for v in input().split()] for _ in range(N)]

direction = [
    (0, 1, (0, 2, 4, 3, 5, 1)),
    (0, -1, (0, 5, 1, 3, 2, 4)),
    (-1, 0, (5, 1, 0, 2, 4, 3)),
    (1, 0, (2, 1, 3, 5, 4, 0)),
]
dice = [0, 0, 0, 0, 0, 0]
for v in map(int, input().split()):
    dx, dy, convert = direction[v - 1]
    if 0 <= x + dx < N and 0 <= y + dy < M:
        x += dx
        y += dy
        dice = [dice[i] for i in convert]
        if L[x][y] == 0:
            L[x][y] = dice[5]
        else:
            dice[5], L[x][y] = L[x][y], 0
        print(dice[2])
