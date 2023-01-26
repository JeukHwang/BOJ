counter = 0
P, N, Z = [], [], False
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        counter += 1
    elif n > 0:
        P.append(n)
    elif n < 0:
        N.append(n)
    else:
        Z = True
P.sort(reverse=True)
N.sort()

counter += sum(P[i - 1] * P[i] for i in range(1, len(P), 2))
counter += sum(N[i - 1] * N[i] for i in range(1, len(N), 2))
counter += P[-1] if len(P) % 2 == 1 else 0
counter += N[-1] if len(N) % 2 == 1 and not Z else 0
print(counter)
