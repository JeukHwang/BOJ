N, M = map(int, input().split())
L = [input() for _ in range(N)]

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
counter, d = 1, -1
visited = set()
stack, stack_ = [(0, 0, 1)], []
while stack:
    for x_, y_, can_punch in stack:
        if (x_, y_, can_punch) in visited:
            continue
        visited.add((x_, y_, can_punch))
        if x_ == N - 1 and y_ == M - 1:
            d, stack_ = counter, []
            break
        for dx, dy in direction:
            x, y = x_ + dx, y_ + dy
            if 0 <= x < N and 0 <= y < M:
                if L[x][y] == "0":
                    stack_.append((x, y, can_punch))
                elif can_punch:
                    stack_.append((x, y, False))
    stack, stack_ = stack_, []
    counter += 1
print(d)
