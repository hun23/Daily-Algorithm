N, K = map(int, input().split())
stat_list = [tuple(map(int, input().split())) for _ in range(N)]

ans = 1_000_000 * 3
jinsu = [0, 0, 0]
for i in range(N):
    jinsu[0] = stat_list[i][0]
    for j in range(N):
        jinsu[1] = stat_list[j][1]
        for k in range(N):
            jinsu[2] = stat_list[k][2]

            cnt = 0
            for stat in stat_list:
                if jinsu[0] >= stat[0] and jinsu[1] >= stat[1] and jinsu[2] >= stat[2]:
                    cnt += 1

            if cnt >= K:
                temp = sum(jinsu)
                if temp < ans:
                    ans = temp
print(ans)