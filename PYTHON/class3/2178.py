import sys
from collections import deque

# 입력
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().rstrip()))
q = deque()
# 상(dx[0],dy[0]), 하(dx[1],dy[1]) 좌우도 마찬가지
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q.append((0, 0))  # 첫 원소 넣기
arr[0][0] = -1  # 음수로 바꾸기(= 방문했음)
while q:
    r, c = q.popleft()  # 큐에서 빼고
    for i in range(4):  # 상하좌우로 반복
        nr = r + dr[i]
        nc = c + dc[i]
        # 인덱스가 arr 범위를 넘지 않으면서, 양수일때(=아직 방문하지 않음 & 방문가능)
        if n > nr >= 0 and m > nc >= 0 and arr[nr][nc] > 0:
            # 셀값 업데이트(=셀까지 거리 & 방문여부 업데이트)
            arr[nr][nc] = arr[r][c] - 1
            q.append((nr, nc))  # 큐에 넣기

print(arr[n - 1][m - 1] * -1)
