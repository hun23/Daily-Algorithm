def solution(n, m, x, y, r, c, k):
    answer = ""

    # 변수 초기화
    arr = [[""] * m for _ in range(n)]
    start = (x - 1, y - 1)
    end = (r - 1, c - 1)

    # d - l - r - u
    # dr = [1, 0, 0, -1]
    # dc = [0, -1, 1, 0]

    # u - r - l - d
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]

    # DFS
    stack = []
    stack.append(start)
    while stack:
        r, c = stack.pop()
        cur_k = len(arr[r][c])
        if (r, c) == end and cur_k == k:
            answer = arr[r][c]
            break
        if cur_k + 1 > k:
            continue
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if n > nr >= 0 and m > nc >= 0:
                arr[nr][nc] = arr[r][c] + "urld"[d]
                stack.append((nr, nc))
    if answer == "":
        return "impossible"
    return answer


i = [3, 4, 2, 3, 3, 1, 5]
ii = [2, 2, 1, 1, 2, 2, 2]
iii = [3, 3, 1, 2, 3, 3, 4]
print(solution(*i))
print(solution(*ii))
print(solution(*iii))
