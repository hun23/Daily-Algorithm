N, E = map(int, input().split())
graph = {key: list() for key in range(1, N + 1)}
for e in range(E):
    st, ed, cost = map(int, input().split())
    graph[st].append((ed, cost))
print(graph)

# 먼저 BFS로 불가능하지 않은지 검색
# 1, N, 필수경로가 한 묶음일 필요가 있다.
# 유니온파인드???
