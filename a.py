from collections import deque


def solution(board, aloc, bloc):
    def bfs(rlen, clen, dr, dc, board, fr, to):
        # for b in board:
        #     print(f"bfs:{b}")
        visited = [[0 for _ in range(clen)] for _ in range(rlen)]
        for r in range(rlen):
            for c in range(clen):
                visited[r][c] = board[r][c]
        q = deque()
        q.append(fr)
        while q:
            point = q.popleft()
            dis = visited[point[0]][point[1]]
            for i in range(4):
                nr = point[0] + dr[i]
                nc = point[1] + dc[i]
                if rlen > nr >= 0 and clen > nc >= 0:
                    if visited[nr][nc] == 1:
                        visited[nr][nc] = dis + 1
                        q.append((nr, nc))
        return visited

    def first_to_second_away(board, floc, sloc):
        cnt = 0
        rlen = len(board)
        clen = len(board[0])
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        # a_to_b, b_away_a
        while True:
            # a_to_b
            # bfs(b, a)
            d = bfs(rlen, clen, dr, dc, board, sloc, floc)
            # a가 가능한 경로 중 가장 작은 값 선택
            mind = 1000
            to = [0, 0]
            for i in range(4):
                nr = floc[0] + dr[i]
                nc = floc[1] + dc[i]
                if rlen > nr >= 0 and clen > nc >= 0:
                    if (
                        d[nr][nc] < mind and board[nr][nc] != 0
                    ):  # 최소값이 여러개면?
                        mind = d[nr][nc]
                        to = [nr, nc]
                # 이동이 불가능한 경우
            if to == [0, 0]:
                break
                # 이동 및 board 업데이트 및 횟수 증가
            cnt += 1
            board[floc[0]][floc[1]] = 0
            floc = [to[0], to[1]]
            print(f"floc: {floc}")
            # for b in board:
            #     print(b)
            # b_away_a
            # bfs(a, b)
            d = bfs(rlen, clen, dr, dc, board, floc, sloc)
            # b가 가능한 경로 중 가장 큰 값 선택
            maxd = 0
            to = [0, 0]
            for i in range(4):
                nr = sloc[0] + dr[i]
                nc = sloc[1] + dc[i]
                if rlen > nr >= 0 and clen > nc >= 0:
                    if (
                        d[nr][nc] > maxd and board[nr][nc] != 0
                    ):  # 최소값이 여러개면?
                        maxd = d[nr][nc]
                        to = [nr, nc]
                # 이동이 불가능한 경우
            if to == [0, 0]:
                break
                # 이동 및 board 업데이트 및 횟수 증가
            cnt += 1
            board[sloc[0]][sloc[1]] = 0
            sloc = [to[0], to[1]]
            print(f"sloc: {sloc}")
            # for b in board:
            #     print(b)
        return cnt

    answer = 0
    print(first_to_second_away(board, aloc, bloc))
    print(first_to_second_away(board, bloc, aloc))
    # answer = min(first_to_second_away(board, aloc, bloc), first_to_second_away(board, bloc, aloc))

    return answer


# a_to_b -> a ~ b 최단거리 구해서 가장 낮은 경로 선택
# a_away_b -> a ~ b 최단거리 구해서 가장 큰 경로 선택
# 경로 구하는 방법... 다익스트라?
# a로부터 시작해서 b가 갈 수 있는 곳까지 다익스트라 or bfs로 비용 구하기
# move_a
# update_board
# move_b
# update_board
# 반복

# 누가 이기고 지는지는 어떻게...?
# 경우의 수 판단 (to,to) (to, away), (away, to), (away, away)
# 일단 (to, away) (away, to) 비교해서 작은걸 고르면 될듯
