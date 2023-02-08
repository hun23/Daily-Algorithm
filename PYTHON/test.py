from collections import deque


def solution(maps):
    answer = []
    rlen = len(maps)
    clen = len(maps[0])

    maps = [list(mp) for mp in maps]
    visited = [[False] * clen for _ in range(rlen)]

    cnt = 0
    for r in range(rlen):
        for c in range(clen):
            if maps[r][c] == "X":
                visited[r][c] = True
            else:
                cnt += 1
    if cnt == 0:
        return [-1]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for r in range(rlen):
        for c in range(clen):
            if not visited[r][c]:
                # BFS
                sum_ = 0
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                while q:
                    r, c = q.popleft()
                    sum_ += int(maps[r][c])
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if rlen > nr >= 0 and clen > nc >= 0:
                            if not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                if sum_ != 0:
                    answer.append(sum_)
    return sorted(answer)


s = solution(["X591X", "X1X5X", "X231X", "1XXX1"])
print(s)
# 코드 비교 필요
