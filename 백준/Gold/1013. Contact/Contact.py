import re

for _ in range(int(input())):
    print("YES" if re.search("^(100+1+|01)+$", input()) is not None else "NO")
