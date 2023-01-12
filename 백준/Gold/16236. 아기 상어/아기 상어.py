def find_init_pos(N, M):
    for i in range(N):
        for j in range(N):
            if M[i][j] == 9:
                return i, j


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def search_prey(N, M, size, current_pos):
    stack, stack_, prey = [current_pos], [], []
    dist = 0
    visited = set()
    while stack and not prey:
        dist += 1
        for (x, y) in stack:
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for (i, j) in direction:
                x_, y_ = x + i, y + j
                if (0 <= x_ < N) and (0 <= y_ < N):
                    if 0 < M[x_][y_] < size:
                        prey.append((x_, y_))
                    elif M[x_][y_] == 0 or M[x_][y_] == size:
                        stack_.append((x_, y_))
        stack = stack_
        stack_ = []
    if prey:
        prey.sort()
        return prey[0], dist
    else:
        return None, 0


def hunt():
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    pos = find_init_pos(N, M)
    M[pos[0]][pos[1]] = 0
    time, size, eat = 0, 2, 0
    while True:
        pos, dist = search_prey(N, M, size, pos)
        if pos is None:
            break
        M[pos[0]][pos[1]] = 0
        time += dist
        eat += 1
        if size == eat:
            size += 1
            eat = 0
    print(time)


hunt()
