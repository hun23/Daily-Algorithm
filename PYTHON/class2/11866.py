import sys
from collections import deque

n ,k = map(int, sys.stdin.readline().rstrip().split())
# deque 만들고 1 ~ n까지 입력
que = deque()
for i in range(1, n + 1):
    que.append(i)
# k번째 찾기 위한 변수
kill = 1
answer = []
while (que):
    # 일단 왼쪽에서 뽑고
    temp = que.popleft()
    if kill % k != 0:
        # k번째가 아니면 뒤로(원형이라 상관x)
        que.append(temp)
    else:
        # k번째인 경우 다시 append하지 않음(=제거)
        answer.append(temp)
        # 카운트 초기화
        kill = 0
    kill += 1
# 출력형식 맞추기
pr = "<"
for (i, a) in enumerate(answer):
    pr += str(a) + (", " if i != len(answer) - 1 else "")
pr += ">"
print(pr)