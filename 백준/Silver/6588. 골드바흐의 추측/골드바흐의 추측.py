memo = {2: True}


def is_prime(n):
    if n in memo:
        return memo[n]
    for i in range(2, int(n**0.5) + 1):
        if is_prime(i) and n % i == 0:
            memo[n] = False
            return False
    memo[n] = True
    return True


while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n // 2 + 1, 2):
        if is_prime(i) and is_prime(n - i):
            print(f"{n} = {i} + {n-i}")
            break
