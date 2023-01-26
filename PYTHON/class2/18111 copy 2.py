import sys
from tqdm import tqdm
import time as ttime

# 시간초과 2 500 * 500에 13.424108028411865
# 입력
# n, m, b_inp = map(int, input().split())
st = ttime.time()
f = open("./TESTCASE/18111.txt")
n, m, b_inp = map(int, f.readline().rstrip().split())
arr = [0 for _ in range(m)]
for i in range(n):
    # arr[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = list(map(int, f.readline().rstrip().split()))
# 변수 세팅
get_block_time = 2
put_block_time = 1
answer = (-1, -1)

# 0 ~ 256까지 전부 고려하기
for h in tqdm(range(257)):
    # b : 현재블록, possible : 현재 h가 가능한지, time : 걸리는 시간
    b = b_inp
    possible = True
    time = 0
    # arr 순회
    for row in range(n):
        for col in range(m):
            # 목표 높이(h)와 현재 칸의 높이(arr[row][col]) 차이
            diff = arr[row][col] - h
            if diff > 0:
                b += diff  # diff가 양수면 인벤토리에 블록 저장
                time += get_block_time * diff
            else:
                b += diff  # diff가 음수인 상태이므로 += 사용
                time -= put_block_time * diff  # 같은 이유로 -= 사용
            # 인벤토리가 음수이거나, 시간이 기존보다 더 걸리면
            if b < 0 or (answer[0] != -1 and time > answer[0]):
                possible = False  # 불가능
                break
        if not possible:
            break
    if possible:
        answer = (time, h)
print(f"{answer[0]} {answer[1]}")
print(f"time: {ttime.time() - st}")
