import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
di = dict()
for n in range(N):
    addrs, pw = sys.stdin.readline().rstrip().split()
    di[addrs] = pw
for m in range(M):
    print(di[sys.stdin.readline().rstrip()])
