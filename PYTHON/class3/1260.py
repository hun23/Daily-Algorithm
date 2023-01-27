import sys
from collections import deque


def dfs(graph, visited, answer, current_node):
    # 방문시 answer에 추가
    answer.append(str(current_node))
    # 방문체크
    visited[current_node] = True
    for node in graph[current_node]:
        if not visited[node]:  # 방문하지 않았으면
            dfs(graph, visited, answer, node)  # 재귀


def bfs(graph, visited, answer, queue, current_node):
    # 첫 요소 방문 체크 및 queue에 append
    visited[current_node] = True
    queue.append(current_node)
    # queue가 빌 때까지
    while len(queue) != 0:
        # queue의 맨 앞에서 하나 뽑아서
        current_node = queue.popleft()
        answer.append(str(current_node))
        # 해당 노드와 연결된 노드를 순회
        for node in graph[current_node]:
            # 방문하지 않았으면
            if not visited[node]:
                # 방문 체크 및 queue에 넣기
                visited[node] = True
                queue.append(node)


n, m, v = map(int, input().split())
# graph node가 1번부터 시작하기 때문에 visited, graph 모두 0번을 미리 추가함
# DFS
visited = [False] * (n + 1)
graph = [set() for _ in range(n + 1)]
new_graph = []
answer = []

# 그래프 그리기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

# 노드 순서 오름차순 정렬(작은 노드부터 방문하기 위해)
for node in graph:
    new_graph.append(sorted(list(node)))
dfs(new_graph, visited, answer, v)  # DFS 실행
print(" ".join(answer))

# 그래프 입력하는 남의코드
# 인접행렬방법, 공간복잡도 O(n^2) 비효율
# 공간적으로는 비어있든 말든 총(n + 1)**2 개의 공간을 할당하니 낭비
# 보기 편하고, 따로 sort할 필요 없다는 장점
# 나중에 반복문돌때 인덱스로 돌아야해서 귀찮을지도?
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = graph[b][a] = 1

# 그래프 입력하는 또하나의 코드
# 인접리스트
# 다른 언어는 연결리스트 사용, 파이썬이니까 딕셔너리 사용
# 공간복잡도 O(n + m), n은 노드 개수, m은 에지(간선) 개수
graph = {1: [1, 3, 4], 2: [4], 3: [4], 4: [1]}


# BFS 위한 초기화
visited = [False] * (n + 1)
answer = []
queue = deque()
bfs(new_graph, visited, answer, queue, v)  # BFS 실행
print(" ".join(answer))
