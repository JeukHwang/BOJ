I = input()
F = list(map(int, set(I) - set("01")))
number = int(I)
if all(number % i == 0 for i in F):
    print(number)
else:
    digit = 1
    while True:
        number_ = number * 10**digit
        for j in range(0, 10**digit):
            if all((number_ + j) % i == 0 for i in F):
                print(number_ + j)
                break
        else:
            digit += 1
            continue
        break
