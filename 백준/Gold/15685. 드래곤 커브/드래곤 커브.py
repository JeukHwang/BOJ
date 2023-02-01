direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
pss = set()
for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    s = (x + direction[d][0], y + direction[d][1])
    ps = set([(x, y), s])
    for _ in range(g):
        ps.update([(-p[1] + s[1] + s[0], p[0] - s[0] + s[1]) for p in ps])
        s = (-y + s[1] + s[0], x - s[0] + s[1])
    pss.update(ps)
counter = 0
for i in range(0, 100):
    for j in range(0, 100):
        if len(pss.intersection([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])) == 4:
            counter += 1
print(counter)
