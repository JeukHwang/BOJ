memo = {1: False, 2: True}


def is_prime(n):
    if n not in memo:
        flag = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                flag = False
                break
        memo[n] = flag
    return memo[n]


N = int(input())
while True:
    if str(N) == str(N)[::-1] and is_prime(N):
        print(N)
        break
    N += 1
