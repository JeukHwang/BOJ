memo = {1: False, 2: True}


def is_prime(n):
    if n not in memo:
        memo[n] = not any(
            is_prime(i) and n % i == 0 for i in range(2, int(n**0.5) + 1)
        )
    return memo[n]


for _ in range(int(input())):
    A, B = map(int, input().split())
    if A == B:
        print(0)
        continue
    stack, stack_, visited = [A], [], set()
    counter = 0
    while True:
        for v in stack:
            if (v not in visited) and is_prime(v):
                visited.add(v)
                a, b, c, d = v // 1000, v // 100 % 10, v // 10 % 10, v % 10
                stack_.extend(n * 1000 + b * 100 + c * 10 + d for n in range(1, 10))
                stack_.extend(a * 1000 + n * 100 + c * 10 + d for n in range(10))
                stack_.extend(a * 1000 + b * 100 + n * 10 + d for n in range(10))
                stack_.extend(a * 1000 + b * 100 + c * 10 + n for n in range(10))
        stack, stack_ = stack_, []
        counter += 1
        if not stack:
            print("Impossible")
            break
        if B in stack:
            print(counter)
            break
