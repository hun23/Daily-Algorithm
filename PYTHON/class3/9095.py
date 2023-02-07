from collections import deque

T = int(input())
# d = {key:0 for key in range(11)}
# d[1] = 1
# d[2] = 2
# d[3] = 4
for tc in range(T):
    n = int(input())
    # BFS / DFS로 0이 될때마다 count?
    # dp?
    # i = 1
    # while i <= n:
    # if d[i] != 0:

    # bfs로 0이 될때까지
    cnt = 0
    visited = [False] * (n + 1)
    q = deque()
    q.append(n)
    while q:
        cur = q.popleft()
        for i in range(1, 4):
            new = cur - i
            if new == 0:
                cnt += 1
            elif new > 0:
                # if not visited[new] and new > 0:
                # visited[new] = True
                q.append(new)
    print(cnt)
