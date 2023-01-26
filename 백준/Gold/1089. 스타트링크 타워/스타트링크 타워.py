N = int(input())
M = [input() for _ in range(5)]

D_ = [
    "####.##.##.####",
    "..#..#..#..#..#",
    "###..#####..###",
    "###..####..####",
    "#.##.####..#..#",
    "####..###..####",
    "####..####.####",
    "###..#..#..#..#",
    "####.#####.####",
    "####.####..####",
]
D = [set(i for i in range(15) if d[i] == "#") for d in D_]


ans = 0
for i in range(N):
    d_ = "".join(m[4 * i : 4 * i + 3] for m in M)
    d = set(i for i in range(15) if d_[i] == "#")
    possible = [i for i in range(10) if D[i].issuperset(d)]
    if not possible:
        ans = -1
        break
    ans = ans * 10 + sum(possible) / len(possible)
print(ans)
