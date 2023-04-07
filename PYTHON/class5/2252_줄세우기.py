from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())
graph = {key: [] for key in range(1, N + 1)}
indegree = [0] * (N + 1)
for m in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    indegree[b] += 1
answer = []
q = deque()
for n in range(1, N + 1):
    if indegree[n] == 0:
        q.append(n)

while q:
    cur = q.popleft()
    answer.append(cur)
    for nex in graph[cur]:
        indegree[nex] -= 1
        if indegree[nex] == 0:
            q.append(nex)
print(*answer)
