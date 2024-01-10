N, K = map(int, input().split())
stat_list = [tuple(map(int, input().split())) for _ in range(N)]
str_sorted = [stat[0] for stat in sorted(stat_list, key=lambda x:x[0])]
dex_sorted = [stat[1] for stat in sorted(stat_list, key=lambda x:x[1])]
int_sorted = sorted(stat_list, key=lambda x:x[2])

ans = 1_000_000 * 3
for strength in str_sorted[K - 1:]:
    for dexterity in dex_sorted[K - 1:]:
        cnt = 0
        for s, d, intelligence in int_sorted:
            if strength >= s and dexterity >= d:
                cnt += 1
                if cnt == K:
                    ans = min(ans, strength + dexterity + intelligence)
                    break
print(ans)
