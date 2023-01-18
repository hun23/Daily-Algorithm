import sys

def choose(arr, used, answer, depth, sum):
    # depth == 3, 카드 3장을 찾기
    if depth == 3:
        answer.append(sum)
        return
    for (i, num) in enumerate(arr):
        # 해당 arr index의 카드를 사용하지 않았으면
        if not used[i]:
            used[i] = True
            sum += num
            # 합이 초과하지 않는 경우에만 다음 재귀 진행
            if sum <= m:
                choose(arr, used, answer, depth + 1, sum)
            # 다음 arr index로 넘어가기 전에 sum, used 초기화
            sum -= num
            used[i] = False
    return

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
used = [False for _ in range(n)]
# 경우의 수(<=m) 담을 리스트
answer = []
# 재귀함수 시작
choose(arr, used, answer, depth=0, sum=0)
print(max(answer))