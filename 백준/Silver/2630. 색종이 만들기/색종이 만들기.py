N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]


def quad(i0, i1, j0, j1):
    s = sum(sum(M[i][j0:j1]) for i in range(i0, i1))
    if s == 0:
        return (1, 0)
    elif s == (j1 - j0) * (i1 - i0):
        return (0, 1)
    else:
        im, jm = (i0 + i1) // 2, (j0 + j1) // 2
        q10, q11 = quad(i0, im, j0, jm)
        q20, q21 = quad(im, i1, j0, jm)
        q30, q31 = quad(i0, im, jm, j1)
        q40, q41 = quad(im, i1, jm, j1)
        return (q10 + q20 + q30 + q40, q11 + q21 + q31 + q41)


a, b = quad(0, N, 0, N)
print(a)
print(b)
