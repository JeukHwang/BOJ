memo = {1: False, 2: True}


def is_prime(n):
    if n not in memo:
        flag = True
        for i in range(2, int(n**0.5) + 1):
            if is_prime(i) and n % i == 0:
                flag = False
                break
        memo[n] = flag
    return memo[n]


memo_prime = {}


def prime_number(n):
    if is_prime(n):
        memo_prime[n] = 1
        return memo_prime[n]
    else:
        for i in range(2, int(n**0.5) + 1):
            if is_prime(i) and n % i == 0:
                memo_prime[n] = prime_number(n // i) + 1
                return memo_prime[n]


def is_under_prime(n):
    return is_prime(prime_number(n))


A, B = map(int, input().split())
print(sum(1 for i in range(A, B + 1) if is_under_prime(i)))
