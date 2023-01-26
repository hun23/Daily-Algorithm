import sys
from tqdm import tqdm
import time as ttime

# 시간초과 3 500 * 500에 10.372531414031982
# 입력
# n, m, b_inp = map(int, input().split())
st = ttime.time()
f = open("./TESTCASE/18111.txt")
n, m, b_inp = map(int, f.readline().rstrip().split())
arr = [0 for _ in range(m)]
_min = 256
_max = 0
for i in range(n):
    # arr[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = list(map(int, f.readline().rstrip().split()))
    if _min > min(arr[i]):
        _min = min(arr[i])
    if _max < max(arr[i]):
        _max = max(arr[i])
# 변수 세팅
get_block_time = 2
put_block_time = 1
answer = (2147483647, -1)
# 0 ~ 256까지 전부 고려하기
for h in tqdm(range(_max, _min - 1, -1)):
    # b : 현재블록, possible : 현재 h가 가능한지, time : 걸리는 시간
    b = b_inp
    time = answer[0]
    time_out = False
    # arr 순회
    for row in range(n):
        for col in range(m):
            # 목표 높이(h)와 현재 칸의 높이(arr[row][col]) 차이
            diff = arr[row][col] - h
            if diff > 0:
                b += diff  # diff가 양수면 인벤토리에 블록 저장
                time -= get_block_time * diff  # time에서 소모된 시간 빼기
            else:
                b += diff  # diff가 음수인 상태이므로 += 사용
                time += put_block_time * diff  # 같은 이유로 += 사용
            if time < 0:
                time_out = True
                break
        if time_out:
            break
    # 인벤토리가 음수이면
    if b < 0 or time_out:
        continue
    answer = (answer[0] - time, h)
print(f"{answer[0]} {answer[1]}")
print(f"time: {ttime.time() - st}")
