L = []
for _ in range(int(input())):
    command, *args = input().split()
    try:
        getattr(L, command)(*[int(x) for x in args])
    except AttributeError:
        print(L)
