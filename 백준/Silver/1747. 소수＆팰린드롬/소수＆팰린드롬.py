def is_prime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


N = int(input())
while True:
    if str(N) == str(N)[::-1] and is_prime(N):
        print(N)
        break
    N += 1
