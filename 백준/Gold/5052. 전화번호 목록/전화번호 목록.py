import sys

I = sys.stdin.readline
for _ in range(int(I())):
    n = int(I())
    L = sorted(I().rstrip() for _ in range(n))
    for i in range(n - 1):
        if L[i] == L[i + 1][: len(L[i])]:
            print("NO")
            break
    else:
        print("YES")
