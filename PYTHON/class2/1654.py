import sys


def ok(arr, _len, n):
    count = 0
    for k in arr:
        count += k // _len
    if count >= n:
        return True
    else:
        return False


k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))
hi = max(arr)
lo = 1
if ok(arr, lo, n) == ok(arr, hi, n):
    print(hi)
else:
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if ok(arr, lo, n) == ok(arr, mid, n):
            lo = mid
        elif ok(arr, hi, n) == ok(arr, mid, n):
            hi = mid
    print(lo)
