# with open("./sample_input.txt", "r") as fr:

for tc in range(1, 11):
    V, E = map(int, input().split())
    inp = list(map(int, input().split()))
    # V, E = map(int, fr.readline().rstrip().split())
    # inp = list(map(int, fr.readline().rstrip().split()))
    graph = {key: [] for key in range(1, V + 1)}
    reverse_graph = {key: [] for key in range(1, V + 1)}
    visited = [False] * (V + 1)
    answer = []
    for i in range(0, len(inp), 2):
        graph[inp[i]].append(inp[i + 1])
        reverse_graph[inp[i + 1]].append(inp[i])
    for k, v in reverse_graph.items():
        if len(v) != 0:
            continue
        # DFS
        stack = []
        stack.append(k)
        while stack:
            cur = stack.pop()
            nexts = graph[cur]
            if not visited[cur]:
                answer.append(str(cur))
                visited[cur] = True
                for nex in nexts:
                    reverse_graph[nex].remove(cur)
                    if len(reverse_graph[nex]) == 0:
                        stack.append(nex)
    print(f"#{tc} ", end="")
    print(" ".join(answer))
