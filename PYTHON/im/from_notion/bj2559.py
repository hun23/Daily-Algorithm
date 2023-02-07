N, K = map(int, input().split())
arr = list(map(int, input().split()))
mx = -2147483647
for i in range(N - K + 1):
    if i == 0:
        s = sum(arr[:K])  # 0인 경우 0번째 ~ K - 1번째 값의 합
    else:  # 아닌 경우 i - 1 번째 원소를 빼고, i - 1 + K 번째 원소 더함
        s = s - arr[i - 1] + arr[i + K - 1]
    if s > mx:
        mx = s
print(mx)
