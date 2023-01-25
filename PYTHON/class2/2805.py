import sys

# 이분탐색 체크용 함수
def check(arr, m, h):
    _sum = 0
    for a in arr:
        if a > h:
            _sum += a - h
    return True if _sum >= m else False


# n, m = map(int, input().split())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
f = open(
    "C:\\Users\\SSAFY\\Desktop\\ssafy\\Daily-Algorithm\\TESTCASE\\2805.txt"
)
n, m = map(int, f.readline().split())
arr = list(map(int, f.readline().rstrip().split()))
lo = 0
hi = max(arr)
j = 0
# 이분탐색
while lo + 1 < hi:
    mid = (lo + hi) // 2
    print(f"{j}: {mid}")
    j += 1
    mid_checked = check(arr, m, mid)  # mid값에서 나누기가 가능한지
    if mid_checked:  # 가능하다면 lo값을 올린다.
        lo = mid
    else:
        hi = mid
    # 기존처럼 네번씩 arr를 순회할 필요가 없다!
    # if check(arr, m, lo) != check(arr, m, mid):
    #     hi = mid
    # elif check(arr, m, mid) != check(arr, m, hi):
    #     lo = mid
print(lo)
