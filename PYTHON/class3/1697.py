from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append(N)  # N 에서 시작
# BFS
while q:
    cur_idx = q.popleft()
    if cur_idx == K:  # K 에 도착하면
        break

    # 걷기
    for i in range(-1, 2):
        if i == 0:
            continue
        next_idx = cur_idx + i
        if 100000 >= next_idx >= 0 and visited[next_idx] != 0:
            visited[next_idx] = visited[cur_idx] + 1  # 현재거리 + 1 넣기
            q.append(next_idx)

    # 순간이동
    next_idx = cur_idx * 2
    if 100000 >= next_idx >= 0 and visited[next_idx] != 0:
        visited[next_idx] = visited[cur_idx] + 1  # 현재거리 + 1 넣기
        q.append(next_idx)
print(visited[K])
