def check(bingo, r, c):
    ret = 0
    li = [0, 0, 0, 0]  # ver, hor, d1, d2
    for i in range(5):
        if bingo[i][c] == -1:  # 세로
            li[0] += 1
        if bingo[r][i] == -1:  # 가로
            li[1] += 1
        if r == c:
            if bingo[i][i] == -1:
                li[2] += 1
        if r + c == 4:
            if bingo[i][4 - i] == -1:
                li[3] += 1
    for l in li:
        if l == 5:
            ret += 1
    return ret


bingo = [list(map(int, input().split())) for _ in range(5)]
arr = []
for _ in range(5):
    arr.extend(list(map(int, input().split())))
cnt = 0
for (i, num) in enumerate(arr):
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == num:
                bingo[r][c] = -1
                cnt += check(bingo, r, c)
    if cnt >= 3:
        print(i + 1)
        break
