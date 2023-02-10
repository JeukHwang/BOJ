import sys

I = sys.stdin.readline
for _ in range(int(I())):
    n = int(I())
    L = sorted(I().rstrip() for _ in range(n))
    is_consistant = any(L[i] == L[i + 1][: len(L[i])] for i in range(n - 1))
    print("YES" if not is_consistant else "NO")
