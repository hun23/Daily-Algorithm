import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = {key: [] for key in range(1, N + 1)}  # dictionary 초기화
for _ in range(M):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append(e)  # 그래프 연결
    graph[e].append(s)
# DFS
count = 0
stack = []
visited = [False] * (N + 1)
for i in range(1, N + 1):
    stack.append(i)
    cycled = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            cycled = 1
            visited[node] = True
            for n in graph[node]:
                stack.append(n)
    count += cycled
print(count)


# BFS
count = 0
q = deque()
visited = [False] * (N + 1)
for i in range(1, N + 1):  # 각 정점을 시작 지점으로 하며 count
    q.append(i)
    cycled = 0
    while q:
        nodes = graph[q.popleft()]
        for node in nodes:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                cycled = 1
    count += cycled
print(count)
