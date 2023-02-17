from collections import deque

M, N = map(int, input().split())
K = int(input())
coordinates = {key: [] for key in range(1, K + 1)}
graph = {key: [] for key in range(1, K + 1)}
for k in range(K):  # get Bus Coordinates
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            coordinates[b].append((x, y))
sx, sy, ex, ey = map(int, input().split())  # get end point

# Bus coordinates to bus numbers
for coordinate in coordinates.items():
    for c in coordinate:
        

# BFS
visited = [[False] * (1 + M) for _ in range(1 + N)]
q = deque()
q.append((sx, sy))
visited[sy][sx] = True
while q:
    x, y = q.popleft()
    for nex in graph[]
