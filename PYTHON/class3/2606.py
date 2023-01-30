import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
di = defaultdict(list)
for _ in range(c):
    k, v = map(int, sys.stdin.readline().rstrip().split())
    di[k].append(v)
    di[v].append(k)
# bfs
# q = deque()
# q.append(1)
# visited = [False] * (n + 1)
# count = 0
# while q:
#     nexts = di[q.popleft()]
#     for next in nexts:
#         if not visited[next]:
#             visited[next] = True
#             q.append(next)
#             count += 1
# print(count - 1)

# dfs
stack = []
stack.append(1)
visited = [False] * (n + 1)
count = 0
while stack:
    cur = stack.pop()
    if not visited[cur]:
        visited[cur] = True
        count += 1
        for next in di[cur]:
            stack.append(next)
print(count - 1)
