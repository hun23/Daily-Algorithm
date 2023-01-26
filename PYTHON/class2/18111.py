import sys
from tqdm import tqdm
import time as ttime

# 통과, 500 * 500 시간: 0.09084129333496094
# 입력
st = ttime.time()
f = open("./TESTCASE/18111.txt")
# n, m, b_inp = map(int, input().split())
n, m, b_inp = map(int, f.readline().rstrip().split())
# arr 입력 및 정렬
arr = [0 for _ in range(n * m)]
height_count = dict()  # 이번 문제 핵심
for row in range(n):
    # inp = list(map(int, sys.stdin.readline().rstrip().split()))
    inp = list(map(int, f.readline().rstrip().split()))
    for (i, num) in enumerate(inp):
        if height_count.get(num) == None:
            height_count[num] = 1
        else:
            height_count[num] += 1
        arr[row * m + i] = num
# 변수 세팅
_min = min(arr)
_max = max(arr)
get_block_time = 2
put_block_time = 1
need_time = 2147483647
answer_height = -1
for target_height in range(_min, _max + 1):
    put_need = 0
    get_need = 0
    b = b_inp
    for (height, count) in height_count.items():
        diff = (target_height - height) * count
        if diff >= 0:
            put_need += diff
        else:
            get_need -= diff  # diff가 음수이므로 -= 사용
            b -= diff
    if put_need > b or b < 0:
        continue
    time_sum = put_need * put_block_time + get_need * get_block_time
    if need_time >= time_sum:  # 소모되는 시간이 같으면
        need_time = time_sum
        answer_height = target_height  # 더 높은 값으로 업데이트
print(need_time, end=" ")
print(answer_height)
print(f"time: {ttime.time() - st}")
