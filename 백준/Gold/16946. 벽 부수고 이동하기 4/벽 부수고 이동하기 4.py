N, M = map(int, input().split())
L = [list(map(int, input())) for _ in range(N)]

group = 2
size = [0, 0]
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
for i in range(N):
    for j in range(M):
        if L[i][j] == 0:
            counter = 0
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if L[x][y] != 0:
                    continue
                L[x][y] = group
                counter += 1
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and L[nx][ny] == 0:
                        stack.append((nx, ny))
            group += 1
            size.append(counter)
for i in range(N):
    for j in range(M):
        if L[i][j] != 1:
            print(0, end="")
        else:
            gs = set(
                L[i + di][j + dj]
                for di, dj in direction
                if 0 <= i + di < N and 0 <= j + dj < M
            )
            print((sum(size[g] for g in gs) + 1) % 10, end="")
    print()
