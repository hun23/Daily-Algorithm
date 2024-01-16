import random

def answer(N, K, arr):
    s = sum(arr[0 : 0 + K])  # 처음(인덱스=0) K 까지의 합
    mx = s
    for i in range(1, N - K + 1):  # 인덱스 1부터 N - K 까지
        # 이전 인덱스의 값(arr[i-1])을 빼고 다음 인덱스의 값(arr[i-1 + K]) 더하기
        s = s - arr[i - 1] + arr[i - 1 + K]
        if s > mx:
            mx = s
    return mx
    
def my(N, K, arr):
    prefix_sum = [0] * (N + 1)
    ans = -100 * 100000
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    for i in range(K, N + 1):
        temp = prefix_sum[i] - prefix_sum[i - K]
        if ans < temp:
            ans = temp
    return ans

T = 1000
for t in range(T):
    N = random.randint(2, 100000)
    K = random.randint(1, N)
    arr = [(random.randint(-100, 100)) for _ in range(N)]
    a, b = answer(N, K, arr), my(N, K, arr)
    if a != b:
        print(N, K)
        print(arr)
        print(a, b)