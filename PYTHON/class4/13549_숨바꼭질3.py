from collections import deque

# 펑
# def solve(N, K, cnt):
#     global answer
#     if N == K:
#         if answer > cnt:
#             answer = cnt
#         return
#     elif answer < cnt:
#         return
#
#     # 1 +1
#     solve(N + 1, K, cnt)
#     # 2 -1
#     solve(N - 1, K, cnt)
#     # 3 *2 when N < K
#     if N < K:
#         solve(N * 2, K, cnt + 1)
#     return


def solve_01bfs(N, K):
    visited = [100001] * (100000 + 1)  # 가중치 큰값으로 초기화
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        cur = q.popleft()
        if cur == K:
            return visited[cur]  # 도착하면 가중치 리턴

        # 인덱스 확인 and 현재 경로 가중치 + 필요 가중치 < 다음 경로 가중치
        # jump first because weight = 0
        if cur * 2 < 100001 and visited[cur] + 0 < visited[cur * 2]:
            visited[cur * 2] = visited[cur]
            q.appendleft(cur * 2)
        # move right
        if cur + 1 < 100001 and visited[cur] + 1 < visited[cur + 1]:
            visited[cur + 1] = visited[cur] + 1
            q.append(cur + 1)
        # move left
        if cur - 1 >= 0 and visited[cur] + 1 < visited[cur - 1]:
            visited[cur - 1] = visited[cur] + 1
            q.append(cur - 1)

    return visited[K]


N, K = map(int, input().split())
print(solve_01bfs(N, K))

