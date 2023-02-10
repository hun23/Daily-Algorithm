import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
di = dict()
arr = [""] * (N + 1)
for n in range(N):
    name = sys.stdin.readline().rstrip()
    arr[n + 1] = name
    di[name] = n + 1
for m in range(M):
    inp = sys.stdin.readline().rstrip()
    if inp.isdecimal():
        print(arr[int(inp)])
    else:
        print(di[inp])
