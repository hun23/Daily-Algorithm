import sys

N = int(sys.stdin.readline().strip())
graph = {key: [] for key in range(1, N + 1)}
for n in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [-1] * (N + 1)
# search
stack = [(1, 0)]
while stack:
    cur, parent = stack.pop()
    if tree[cur] == -1:
        tree[cur] = parent
        for nex in graph[cur]:
            stack.append((nex, cur))
for t in tree[2:]:
    print(t)