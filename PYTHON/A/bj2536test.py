from collections import deque
import random
import time
from tqdm import tqdm


def s1(inp):
    global N
    global M
    global K
    graph = {key: set() for key in range(1, K + 1)}
    garo, sero = dict(), dict()
    for k in range(K):  # Bus lines to garo / sero
        b, x1, y1, x2, y2 = map(int, inp[k].split())
        if x1 == x2:  # sero
            y1, y2 = min(y1, y2), max(y1, y2)
            sero.setdefault(x1, []).append((b, y1, y2))
        elif y1 == y2:  # garo
            x1, x2 = min(x1, x2), max(x1, x2)
            garo.setdefault(y1, []).append((b, x1, x2))
    sx, sy, ex, ey = map(
        int, inp[-1].split()
    )  # get start & end point

    # print(garo)
    # print(sero)
    # garo/sero to graph
    garo_keys, sero_keys = list(garo.keys()), list(sero.keys())
    for n, garo_lines in garo.items():
        # garo compare to sero
        for garo_line in garo_lines:
            st, ed = garo_line[1], garo_line[2]
            for sero_key in sero_keys:
                if st <= sero_key <= ed:
                    sero_lines = sero[sero_key]
                    for sero_line in sero_lines:
                        if sero_line[1] <= n <= sero_line[2]:
                            graph[garo_line[0]].add(sero_line[0])
                            graph[sero_line[0]].add(garo_line[0])
        # garo compare to garo
        for i in range(len(garo_lines) - 1):
            for j in range(i + 1, len(garo_lines)):
                if not (
                    garo_lines[i][2] < garo_lines[j][1]
                    or garo_lines[i][1] > garo_lines[j][2]
                ):
                    graph[garo_lines[i][0]].add(garo_lines[j][0])
                    graph[garo_lines[j][0]].add(garo_lines[i][0])
    for m, sero_lines in sero.items():
        # garo compare to garo
        for i in range(len(sero_lines) - 1):
            for j in range(i + 1, len(sero_lines)):
                if not (
                    sero_lines[i][2] < sero_lines[j][1]
                    or sero_lines[i][1] > sero_lines[j][2]
                ):
                    graph[sero_lines[i][0]].add(sero_lines[j][0])
                    graph[sero_lines[j][0]].add(sero_lines[i][0])
    # print(graph)

    # BFS
    visited = [False] * (K + 1)
    q = deque()
    # start point - graph / end point - graph
    start, end = [], []
    try:
        for bnum, st, ed in garo[sy]:
            if st <= sx <= ed:
                start.append(bnum)
    except:
        pass
    try:
        for bnum, st, ed in sero[sx]:
            if st <= sy <= ed:
                start.append(bnum)
    except:
        pass
    try:
        for bnum, st, ed in garo[ey]:
            if st <= ex <= ed:
                end.append(bnum)
    except:
        pass
    try:
        for bnum, st, ed in sero[ex]:
            if st <= ey <= ed:
                end.append(bnum)
    except:
        pass
    for st in start:
        q.append((st, [st]))
        visited[st] = True

    # print(q)
    answer = 0
    while q:
        cur, cnt = q.popleft()
        # print(f"cur:{cur} / {cnt}")
        if cur in end:
            answer = len(cnt)
            break
        for nex in graph[cur]:
            if not visited[nex]:
                visited[nex] = True
                temp = cnt[:]
                temp.append(nex)
                q.append((nex, temp))
    # print(answer)
    return answer


def s2(inp):
    global N
    global M
    global K
    bus_lines = dict()
    arr = [
        [[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)
    ]
    for k in range(K):  # Bus lines to garo / sero
        b, x1, y1, x2, y2 = map(int, inp[k].split())
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        bus_lines[b] = (x1, y1, x2, y2)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                arr[y][x][b] = 1
    # get start & end point
    sx, sy, ex, ey = map(int, inp[-1].split())
    # print(arr)
    q = deque()
    visited = [False] * (1 + K)
    for i in range(K + 1):
        if arr[sy][sx][i] == 1:
            q.append((i, [i]))

    endlines = []
    for j in range(K + 1):
        if arr[ey][ex][j] == 1:
            endlines.append(j)

    while q:
        bus_num, history = q.popleft()
        if bus_num in endlines:
            # print("break")
            # print(history)
            # print(len(history))
            # break
            return len(history)
        x1, y1, x2, y2 = bus_lines[bus_num]
        next_nums = set()
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                possible_lines = arr[y][x]
                for j in range(len(possible_lines)):
                    if possible_lines[j] == 1:
                        next_nums.add(j)
        for nex in next_nums:
            if not visited[nex]:
                visited[nex] = True
                temp = history[:]
                temp.append(nex)
                q.append((nex, temp))
    return 0


T = 100
t1, t2 = 0, 0
for tc in tqdm(range(1, T + 1)):
    # N, M = random.randint(1, 100000), random.randint(1, 100000)
    # K = random.randint(1, 5000)
    N, M = random.randint(2, 1000), random.randint(2, 1000)
    K = random.randint(1, 500)
    inp = []
    # M, N, K = 6, 2, 4
    # inp = [
    #     "1 6 1 6 2",
    #     "2 1 1 1 2",
    #     "3 1 2 6 2",
    #     "4 2 1 2 2",
    #     "2 1 6 1",
    # ]
    for k in range(1, K + 1):
        rand = random.randint(0, 1)
        if rand:  # garo
            x1 = random.randint(1, M - 1)
            x2 = random.randint(x1 + 1, M)
            y1 = y2 = random.randint(1, N)
        else:
            x1 = x2 = random.randint(1, M)
            y1 = random.randint(1, N - 1)
            y2 = random.randint(y1 + 1, N)
        inp.append(f"{k} {x1} {y1} {x2} {y2}")
    sx = random.randint(1, M)
    sy = random.randint(1, N)
    ex = random.randint(1, M)
    ey = random.randint(1, N)
    inp.append(f"{sx} {sy} {ex} {ey}")
    st = time.time()
    a1 = s1(inp)
    mid = time.time()
    a2 = s2(inp)
    ed = time.time()
    t1 += mid - st
    t2 += ed - mid
    # print(a1, a2)
    if a1 != a2:
        print("-------------------------------")
        print(a1, a2)
        print(M, N, K)
        for ip in inp:
            # ss = ip.split()
            # print('"', end="")
            # print(*ss, sep=",", end="")
            # print('"')
            print(ip, sep=",")
        print()
        break
print(f"t1: {t1}")
print(f"t2: {t2}")
