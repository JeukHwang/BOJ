L = [1 for _ in range(10)]
for _ in range(int(input()) - 1):
    for i in range(8, -1, -1):
        L[i] = (L[i] + L[i + 1]) % 10007
print(sum(L) % 10007)
