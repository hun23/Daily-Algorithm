import sys

t = int(input())
answer = []
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    quo, rem = divmod(n, h)
    # 나머지가 0일때 구분
    if rem == 0:
        rem = h
    else:
        quo += 1
    answer.append(rem * 100 + quo)

for a in answer:
    print(a)