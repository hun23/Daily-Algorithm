from collections import deque
import sys


def do_d(n):
    ret = n * 2
    if ret > 9999:
        ret = ret % 10000
    return ret


def do_s(n):
    ret = n - 1
    if ret == -1:
        ret = 9999
    return ret


def do_l(n):
    quo, rem = divmod(n, 1000)
    ret = rem * 10 + quo
    return ret


def do_r(n):
    quo, rem = divmod(n, 10)
    ret = quo + rem * 1000
    return ret


def do(i, n):
    if i == 0:
        return do_d(n)
    elif i == 1:
        return do_s(n)
    elif i == 2:
        return do_l(n)
    elif i == 3:
        return do_r(n)


T = int(sys.stdin.readline().rstrip())
for tc in range(1, T + 1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    visited = [False] * 10000
    q = deque()
    q.append([A, ""])
    while q:
        cur = q.popleft()
        cnum = cur[0]
        ccnt = cur[1]
        if cnum == B:
            answer = ccnt
            break
        for i in range(4):
            nex = do(i, cnum)
            if not visited[nex]:
                visited[nex] = True
                q.append([nex, ccnt + "DSLR"[i]])
    print(answer)
