T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 부분합 생성
    # part_sum[i]는 arr[0] ~ arr[i]까지의 합
    part_sum = [0] * N
    part_sum[0] = arr[0]
    for i in range(1, N):
        part_sum[i] = arr[i] + part_sum[i - 1]
    # 최소 최대 찾기
    mn = 10000 * M + 1 # 이론상 최대합 + 1
    mx = 0 # 최소값
    for i in range(M - 1, N):
        if i == M - 1: # i = M-1이면
            part = part_sum[i]
        else:           # i - M >= 0 이면
            part = part_sum[i] - part_sum[i - M]
        if part > mx:
            mx = part
        if part < mn:
            mn = part
    print(f"#{tc + 1} {mx - mn}")