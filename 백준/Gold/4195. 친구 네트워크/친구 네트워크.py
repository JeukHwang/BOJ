import sys


def union(union_find, counter, a, b):
    a_index = find(union_find, a)
    b_index = find(union_find, b)
    if a_index != b_index:
        union_find[a_index] = b_index
        counter[b_index] += counter[a_index]


def find(union_find, n):
    if union_find[n] != n:
        v = find(union_find, union_find[n])
        union_find[n] = v
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
            COUNTER[ID[A]] = 1
        if B not in ID:
            ID[B] = len(ID)
            UNION_FIND.append(ID[B])
            COUNTER[ID[B]] = 1
        union(UNION_FIND, COUNTER, ID[A], ID[B])
        print(COUNTER[find(UNION_FIND, ID[A])])
