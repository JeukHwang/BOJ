print(
    "\n".join(
        map(str, sorted(set(range(1, 31)) - set(int(input()) for _ in range(28))))
    )
)
