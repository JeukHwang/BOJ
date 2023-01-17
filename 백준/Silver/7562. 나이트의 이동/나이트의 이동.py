direction = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
for _ in range(int(input())):
    L = int(input())
    X1, Y1 = map(int, input().split())
    X2, Y2 = map(int, input().split())
    queue, queue_ = [(X1, Y1)], []
    visited, counter = set(), 0
    while True:
        if (X2, Y2) in queue:
            print(counter)
            break
        for x, y in queue:
            for x_, y_ in direction:
                X, Y = x + x_, y + y_
                if (X, Y) not in visited and 0 <= X < L and 0 <= Y < L:
                    visited.add((X, Y))
                    queue_.append((X, Y))
        queue, queue_ = queue_, []
        counter += 1
