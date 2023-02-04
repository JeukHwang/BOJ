import sys


def union(union_find, counter, a, b):
    max_index = find(union_find, max(a, b))
    min_index = find(union_find, min(a, b))
    if max_index != min_index:
        union_find[max_index] = min_index
        counter[min_index] += counter[max_index]


def find(union_find, n):
    if n != union_find[n]:
        union_find[n] = find(union_find, union_find[n])
    return union_find[n]


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
