import sys

t = int(input())
answer = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    inp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    target = [False for _ in range(n)]
    target[m] = True
    count = 1
    while True:
        mx = max(inp)
        if inp[0] == mx:
            if target[0]:
                answer.append(count)
                break
            del inp[0]
            del target[0]
            count += 1
        else:
            inp.append(inp[0])
            target.append(target[0])
            del inp[0]
            del target[0]
for a in answer:
    print(a)
