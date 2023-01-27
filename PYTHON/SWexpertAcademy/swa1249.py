def get_current_node(arr_time, visited):
    _min = 2147483647
    mr = -1
    mc = -1
    for row in range(len(arr_time)):
        for col in range(len(arr_time)):
            if not visited[row][col]:
                if arr_time[row][col] < _min:
                    _min = arr_time[row][col]
                    mr = row
                    mc = col
    return (mr, mc)


# 1249번
# f = open("./Python/SWexpertAcademy/swa1249input.txt")
t = int(input())
# t = int(f.readline().rstrip())
for tn in range(t):
    n = int(input())
    # n = int(f.readline().rstrip())
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input()))
        # arr[i] = list(map(int, f.readline().rstrip()))
    # Dijkstra Algorithm
    big = 2147483647
    arr_time = [[big] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    arr_time[0][0] = 0
    current_node = (0, 0)
    dr = [1, 0, -1, 0]  # 하 - 우 - 상 - 좌
    dc = [0, 1, 0, -1]

    # 방향탐색
    while True:
        current_node = get_current_node(arr_time, visited)
        r = current_node[0]
        c = current_node[1]
        if r == -1 and c == -1:
            break
        for i in range(4):  # 네방향 체크
            nr = r + dr[i]
            nc = c + dc[i]
            if n > nr >= 0 and n > nc >= 0:  # 방문 가능하면
                # 더 작은 값이면, 값을 갱신한다
                if arr_time[r][c] + arr[nr][nc] < arr_time[nr][nc]:
                    arr_time[nr][nc] = arr_time[r][c] + arr[nr][nc]
        visited[r][c] = True
    print(f"#{tn + 1} {arr_time[n - 1][n - 1]}")
