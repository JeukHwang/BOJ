import sys

I = sys.stdin.readline
for _ in range(int(I())):
    n = int(I())
    L = sorted(I().rstrip() for _ in range(n))
    for i in range(n - 1):
        l1, l2 = len(L[i]), len(L[i + 1])
        if l1 < l2 and L[i] == L[i + 1][:l1]:
            print("NO")
            break
    else:
        print("YES")
