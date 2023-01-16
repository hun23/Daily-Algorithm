n = int(input())
li = []
di = dict()
for _ in range(n):
    x, y = map(int, input().split())
    try:
        di[x].append(y)
    except:
        di[x] = list()
        di[x].append(y)
keys = list(di.keys())
keys.sort()
for key in keys:
    if len(di[key]) == 1:
        print(f"{key} {di[key][0]}")
    else:
        di[key].sort()
        for val in di[key]:
            print(f"{key} {val}")
