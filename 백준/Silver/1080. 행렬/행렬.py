N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

counter = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            counter += 1
            for i_ in range(i, i + 3):
                for j_ in range(j, j + 3):
                    A[i_][j_] = 1 - A[i_][j_]
    if A[i][M - 2] != B[i][M - 2] or A[i][M - 1] != B[i][M - 1]:
        counter = -1
        break
if any(A[i][j] != B[i][j] for i in range(min(N - 2, 0), N) for j in range(M)):
    counter = -1
print(counter)
