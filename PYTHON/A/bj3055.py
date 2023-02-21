from collections import deque

R, C = map(int, input().split())  # R, C <= 50
arr = [[""] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
points = {"D": (0, 0), "S": (0, 0), "*": (0, 0)}
states = dict()
for r in range(R):
    inp = input()
    for c in range(C):
        arr[r][c] = inp[c]
        if inp[c] in "*X":
            visited[r][c] = True
        if inp[c] != ".X":
            points[inp[c]] = (r, c)

# delta
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# BFS
q = deque()
q.append(("*", *points["*"]))
q.append(("S", *points["S"]))
states[("S", *points["S"])] = 0
answer = 0

while q:
    print(q)
    type_, r, c = q.popleft()
    if type_ == "S" and (r, c) == points["D"]:
        answer = states[(type_, r, c)]
        break

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if R > nr >= 0 and C > nc >= 0:
            # water
            if type_ == "*":
                visited[nr][nc] = True
                if arr[nr][nc] not in "XD*":
                    q.append((type_, nr, nc))
            elif type_ == "S":
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    states[(type_, nr, nc)] = (
                        states[(type_, r, c)] + 1
                    )
                    q.append((type_, nr, nc))
print(answer)
