M = 10**9
L = [1 for _ in range(10)]
L[0] = 0
for _ in range(int(input()) - 1):
    L = [
        L[1] if i == 0 else (L[8] if i == 9 else ((L[i - 1] + L[i + 1]) % M))
        for i in range(10)
    ]
print(sum(L) % M)
