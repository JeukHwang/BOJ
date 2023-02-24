N = int(input())
L = list(map(int, input().split()))
V = int(input())


def is_valid_leaf(v):
    if v == V:
        return False
    if L[v] == -1:
        return True
    return is_valid_leaf(L[v])


domain = set(range(N)) - set(L)
if L[V] != -1 and L.count(L[V]) == 1:
    domain.add(L[V])
print([is_valid_leaf(v) for v in domain].count(True))
