N, L = map(int, input().split())
H = sorted(map(int, input().split()))
for h in H:
    if h <= L:
        L += 1
    else:
        break
print(L)
