stack = []
visited = [False for _ in range(7 + 1)]
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

answer = []
stack.append(1)
while stack:
    node = stack.pop()
    if not visited[node]:
        answer.append(node)
        visited[node] = True
        for n in graph[node]:
            stack.append(n)
print(answer)
