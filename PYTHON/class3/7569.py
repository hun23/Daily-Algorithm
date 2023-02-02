from collections import deque

M, N, H = map(int, input().split())
# 토마토 위치 입력
# 입력받으면서 익힐 토마토 개수 세기, 시작점 찾기
boxes = []
start_points = []
tomatoes_to_ripe = 0
for h in range(H):
    box = []
    for n in range(N):
        inp = list(map(int, input().split()))
        box.append(inp)
        for m in range(M):
            if inp[m] == 0:  # 익힐 토마토 개수 카운트
                tomatoes_to_ripe += 1
            elif inp[m] == 1:  # 시작점(익은 토마토)
                start_points.append((h, n, m))
    boxes.append(box)

# BFS, 위 아래 왼쪽 오른쪽 앞 뒤
dm = [0, 0, -1, 1, 0, 0]
dn = [0, 0, 0, 0, 1, -1]
dh = [1, -1, 0, 0, 0, 0]
ripe_count = 0
mx_day = 1  # 죄다 0으로 시작하는 경우에는?
for sp in start_points:
    q = deque()
    q.append(sp)
    while q:
        point = q.popleft()
        days = boxes[point[0]][point[1]][point[2]]
        if days > mx_day:
            mx_day = days
        # 이동 가능 6방향 탐색
        for d in range(6):
            nh = point[0] + dh[d]
            nn = point[1] + dn[d]
            nm = point[2] + dm[d]
            try:
                if boxes[nh][nn][nm] == 0:
                    boxes[nh][nn][nm] = days + 1
                    ripe_count += 1
                    q.append((nh, nn, nm))
            except:
                pass
        for b in boxes:
            for bb in b:
                print(bb)
        print()
print(tomatoes_to_ripe)
print(ripe_count)
if tomatoes_to_ripe > ripe_count:
    print(-1)
else:
    print(mx_day - 1)


# 익은 토마토를 시작으로 BFS하면 될듯?
# get ripe tomatoes
# BFS
# is left?
