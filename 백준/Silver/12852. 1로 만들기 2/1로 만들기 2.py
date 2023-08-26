N = int(input())
L = [None for _ in range(N + 1)]
L[N] = N
S = set([N])
while L[1] is None:
    S_ = set()
    for s in S:
        if L[s - 1] is None:
            L[s - 1] = s
            S_.add(s - 1)
        if L[s // 2] is None and s % 2 == 0:
            L[s // 2] = s
            S_.add(s // 2)
        if L[s // 3] is None and s % 3 == 0:
            L[s // 3] = s
            S_.add(s // 3)
    S = S_
P = [1]
while P[-1] != N:
    P.append(L[P[-1]])
print(len(P) - 1)
print(*reversed(P))
