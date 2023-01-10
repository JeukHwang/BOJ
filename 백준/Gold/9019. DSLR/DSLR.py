DSLR = [
    lambda o: (o * 2) % 10000,
    lambda o: (o + 9999) % 10000,
    lambda o: (o % 1000) * 10 + (o // 1000),
    lambda o: (o % 10) * 1000 + (o // 10),
]

for _ in range(int(input())):
    A, B = map(int, input().split())
    reg = set([A])
    mem = {A: (None, None)}
    while B not in mem:
        reg_new = set()
        for num in reg:
            for i in range(4):
                n = DSLR[i](num)
                if n not in mem:
                    mem[n] = (num, i)
                    reg_new.add(n)
        reg = reg_new

    num = B
    funcs = []
    while True:
        num, func = mem[num]
        if num is None:
            break
        funcs.append(func)
    print("".join("DSLR"[v] for v in funcs[::-1]))
