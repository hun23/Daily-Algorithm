import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())
graph = {key: [] for key in range(1, V + 1)}
for e in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))  # u -> v, with weight w

# dijkstra? - 우선순위 큐 사용
distance = [2147483647] * (1 + V)
# start at K
distance[K] = 0
q = []
heapq.heappush(q, (0, K))
while q:
    cur_d, cur = heapq.heappop(q)
    if distance[cur] < cur_d:
        continue
    # update min distance
    for nex, weight in graph[cur]:
        a = distance[nex]
        b = weight + distance[cur]
        if a > b:
            distance[nex] = min(a, b)
            heapq.heappush(q, (distance[nex], nex))

    # find next node
    if len(q) == 0:
        break

for v in range(1, V + 1):
    if distance[v] == 2147483647:
        print("INF")
    else:
        print(distance[v])

# # dijkstra? - 시간초과
# distance = [float('inf')] * (1 + V)
# visited = [False] * (1 + V)
# # start at K
# distance[K] = 0
# start = K
# while start:
#     # update min distance
#     for nex, weight in graph[start]:
#         a = distance[nex]
#         b = weight + distance[start]
#         distance[nex] = min(a, b)
#     # check visited
#     visited[start] = True
#
#     # find next node
#     min_dis, min_node = float('inf'), 0
#     for i in range(1, V + 1):
#         if not visited[i]:
#             if min_dis > distance[i]:
#                 min_dis = distance[i]
#                 min_node = i
#     start = min_node
# print answer