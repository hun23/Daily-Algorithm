from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starts = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == 2]
print(starts)
q = deque()
q.append(starts)
while q:
