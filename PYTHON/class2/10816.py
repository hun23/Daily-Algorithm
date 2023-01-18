import sys
from tqdm import tqdm
from queue import Queue

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
    # 찾은 값 지우기
    for i in range(start, end):
        del n_arr[start]
    return end - start
        

def count_m(m):
    # 이진탐색
    lo = 0
    hi = len(n_arr) - 1
    while (lo + 1 < hi):
        # 양 끝에 찾는값(m)이 존재하는 경우
        if check(lo, m) == check(hi, m):
            if check(lo, m):
                count = find_range(0, m)
            else:
                count = find_range(len(n_arr) - 1, m)
            di[m] = count
            return count
        # 일반적인 경우
        else:
            mid = int((lo + hi) / 2)
            if check(lo, m) == check(mid, m):
                lo = mid
            elif check(mid, m) == check(hi, m):
                hi = mid
    count = find_range(lo, m)
    di[m] = count
    return count

f = open('C:\\Users\\SSAFY\\Desktop\\ssafy\\Daily-Algorithm\\TESTCASE\\test.txt')
# _n = int(sys.stdin.readline().rstrip())
# n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
# _m = int(sys.stdin.readline().rstrip())
# m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

_n = int(f.readline().rstrip())
n_arr = list(map(int, f.readline().rstrip().split()))
_m = int(f.readline().rstrip())
m_arr = list(map(int, f.readline().rstrip().split()))



# 이진탐색위한 크기순 정렬
n_arr.sort()
# answer = []
answer = Queue()
di = dict()
# m 배열을 순회하며 개수 계산 및 answer에 추가
for m in tqdm(m_arr):
    # 같은 m이 들어온 경우 다시 세는 것을 막기 위해서
    if di.get(m) == None:
        # answer.append(count_m(m))
        answer.put(count_m(m))
    else:
        # answer.append(di[m])
        answer.put(di[m])
# join 이용한 출력

print(' '.join(str(a) for a in answer))