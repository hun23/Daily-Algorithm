import sys


def union(x, y):
    x_rep, y_rep = find_set(x), find_set(y)
    tree[x_rep] = y_rep
    return

def find_set(x):
    to_change = []
    while tree[x] != x:
        to_change.append(x)
        x = tree[x]
    for c in to_change:  # path compression
        tree[c] = x
    return x


V, E = map(int, input().split())
tree = [v for v in range(V + 1)]
inputs = [[0, 0, 0] for _ in range(E)]
for e in range(E):
    for i, v in enumerate(map(int, sys.stdin.readline().rstrip().split())):
        inputs[e][i] = v  # u, v, w
inputs.sort(key=lambda x: x[2])  # sort by weights

idx = 0  # inputs index
answer = 0  # sum of weights
cnt = 0  # number of edges
while cnt < V - 1:
    u, v, w = inputs[idx]
    if find_set(u) != find_set(v):
        union(u, v)
        answer += w
        cnt += 1
    idx += 1
print(answer)