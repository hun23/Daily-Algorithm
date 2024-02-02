from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def update_answer(opened):
    global homes, chickens, ans
    ret = 0
    for home in homes:
        min_dist = 100
        for is_open, chicken in zip(opened, chickens):
            if not is_open:
                continue
            temp_dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            if temp_dist < min_dist:
                min_dist = temp_dist
        ret += min_dist
    ans = min(ans, ret)


def recur(idx, open_cnt, opened):
    global N, M, homes, chickens
    if idx == len(chickens) or open_cnt == M:
        update_answer(opened)
        return
    opened[idx] = True
    recur(idx + 1, open_cnt + 1, opened)
    opened[idx] = False
    recur(idx + 1, open_cnt, opened)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
homes, chickens = [], []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            homes.append((r, c))
        elif arr[r][c] == 2:
            chickens.append((r, c))
opened = [False] * len(chickens)
ans = 2147483647
recur(0, 0, opened)
print(ans)
