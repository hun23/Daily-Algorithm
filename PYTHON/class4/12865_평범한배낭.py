N, K = map(int, input().split())
items = [(0, 0)]  # 0번째 채우기
for n in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
items.sort()  # 무게 오름차순으로 정렬

dp = [0] * (K + 1)  # 가방 무게 K 까지
for i in range(1, N + 1):  # 무게 작은 순서대로
    for j in range(K, items[i][0] -1, -1):
        dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])
print(dp[-1])
