for _ in range(4):
    inp = list(map(int, input().split()))
    minx = 50001
    miny = 50001
    maxx = -1
    maxy = -1
    for i in range(0, 8, 2):
        if i > maxx:
            maxx = i
        if i < minx:
            minx = i
    for j in range(1, 8, 2):
        if j > maxy:
            maxy = j
        if j < miny:
            miny = j
    a = inp[:4]
    b = inp[4:]
    for k in range(4):
        if k % 2 == 0:
            a[k] - minx
            b[k] - minx
        else:
            a[k] - miny
            b[k] - miny

    box = [[] for _ in range(maxy - miny)]
    # box 채우기
    for x in range(a[2] - a[0] + 2):
        box[x] = [2] * (a[3] - a[1] + 2)
        box[x][1:-1] = [1] * (a[3] - a[1])
    cnt = 0
    done = False
    for i in range(len(box)):
        for j in range(len(box[i])):
            b = box[i][j]
            if b == 1:
                done = True
                break
            elif b == 2:
                cnt += 1
        if done:
            break
    if done:
        print("a")
    elif cnt == 1:
        print("c")
    elif cnt > 1:
        print("b")
    else:
        print("d")
