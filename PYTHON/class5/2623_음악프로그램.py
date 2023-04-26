from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
indegrees = []
for n in range(N):
    for i in range(0, len(arr[n]) - 1):
        indegrees[i + 1] = indegrees[i]
q = deque()
