N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


def merge(l, inverse=False):
    nl = [0] * N
    focus = 0 if not inverse else (N - 1)
    direction = 1 if not inverse else -1
    for v in l:
        if v == 0:
            continue
        if nl[focus] == 0:
            nl[focus] = v
        elif nl[focus] == v:
            nl[focus] = v * 2
            focus += direction
        else:
            focus += direction
            nl[focus] = v
    return nl


def transpose(l):
    l_ = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            l_[i][j] = l[j][i]
    return l_


ls, ls_ = [L], []
for i in range(5):
    for l in ls:
        ls_.append([merge(v) for v in l])
        ls_.append([merge(v[::-1], True) for v in l])
        ls_.append(transpose([merge(v) for v in transpose(l)]))
        ls_.append(transpose([merge(v[::-1], True) for v in transpose(l)]))
    ls, ls_ = ls_, []
print(max(j for l in ls for i in l for j in i))
