import sys

sys.stdin = open("input.txt", "r")
import copy

for roop in range(10):
    T = int(input())
    array = []
    for _ in range(100):
        array.append(list(map(int, input().split())))
    xlist = []
    cntlist = []
    for idx in range(100):
        if array[0][idx] == 1:
            xlist.append(idx)
    rst = 2000000
    while xlist != []:
        y = 0
        x = xlist.pop()
        orix = x
        cnt = 0
        newray = copy.deepcopy(array)
        while y != 100:
            if x + 1 < 100 and newray[y][x + 1] == 1:
                newray[y][x] = 0
                x = x + 1
                cnt += 1
            elif x - 1 >= 0 and newray[y][x - 1] == 1:
                newray[y][x] = 0
                x = x - 1
                cnt += 1
            elif y + 1 < 100:
                y = y + 1
                cnt += 1
            else:
                break
        if rst > cnt:
            rst = cnt
            rstidx = orix
        # print(orix, cnt)
    print(f"#{T} {rstidx}")
