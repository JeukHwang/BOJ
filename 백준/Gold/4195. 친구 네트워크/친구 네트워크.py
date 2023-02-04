import sys


def union(a, b):
    global UNION_FIND
    global COUNTER
    a_index = find(a)
    b_index = find(b)
    if a_index != b_index:
        UNION_FIND[a_index] = b_index
        COUNTER[b_index] = (COUNTER[b_index] if b_index in COUNTER else 1) + (
            COUNTER[a_index] if a_index in COUNTER else 1
        )


def find(n):
    global UNION_FIND
    if UNION_FIND[n] != n:
        v = find(UNION_FIND[n])
        UNION_FIND[n] = v
        return v
    else:
        return n


I = sys.stdin.readline
for _ in range(int(I())):
    UNION_FIND = []
    ID = {}
    COUNTER = {}
    for _ in range(int(I())):
        A, B = I().split()
        if A not in ID:
            ID[A] = len(ID)
            UNION_FIND.append(ID[A])
        if B not in ID:
            ID[B] = len(ID)
            UNION_FIND.append(ID[B])
        union(ID[A], ID[B])
        print(COUNTER[find(ID[A])])
