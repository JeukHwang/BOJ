for _ in range(int(input())):
    n = int(input())
    L = [list(map(int, input().split())) for _ in range(2)]
    top, top_, bottom, bottom_ = 0, 0, 0, 0
    for i in range(n):
        _top = max(bottom, bottom_) + L[0][i]
        _bottom = max(top, top_) + L[1][i]
        top, top_, bottom, bottom_ = _top, top, _bottom, bottom
    print(max(top, bottom))
