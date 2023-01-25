import sys

global di
global n_arr


def check(idx, m):
    if n_arr[idx] <= m:
        return False
    return True


def find_range(idx, m):
    # m이 있는 idx를 받은 뒤, m이 몇개인지 세는 함수
    value = n_arr[idx]
    # m이 없는 경우
    if value != m:
        return 0
    start = 0
    end = len(n_arr)
    # idx부터 0으로 세기
    for i in range(idx, -1, -1):
        if value != n_arr[i]:
            start = i + 1
            break
    # idx부터 끝까지 세기
    for i in range(idx, len(n_arr)):
        if value != n_arr[i]:
            end = i
            break
    return end - start


def count_m(m):
    # 이진탐색
    lo = 0
    hi = len(n_arr) - 1
    # 양 끝에 찾는값(m)이 존재하는 경우
    lo_checked = check(lo, m)
    if lo_checked == check(hi, m):
        if lo_checked:
            count = find_range(0, m)
        else:
            count = find_range(len(n_arr) - 1, m)
        di[m] = count
        return count
    while lo + 1 < hi:
        # 일반적인 경우
        mid = (lo + hi) // 2
        lo_checked = check(lo, m)
        mid_checked = check(mid, m)
        if lo_checked != mid_checked:
            hi = mid
        else:
            lo = mid
    count = find_range(lo, m)
    di[m] = count
    return count


_n = int(sys.stdin.readline().rstrip())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
_m = int(sys.stdin.readline().rstrip())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진탐색위한 크기순 정렬
n_arr.sort()
answer = []
di = dict()
# m 배열을 순회하며 개수 계산 및 answer에 추가
for m in m_arr:
    # 같은 m이 들어온 경우 다시 세는 것을 막기 위해서
    if di.get(m) == None:
        answer.append(count_m(m))
    else:
        answer.append(di[m])
print(" ".join(str(a) for a in answer))
