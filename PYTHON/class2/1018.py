import sys
import copy

def check_cell(arr, i, x, j, y):
    count = 0
    color = "W"
    row = i + x
    col = j + y
    if arr[row][col] == color:
        color = "B"
    if x != 0:
        if arr[row - 1][col] != color:
            arr[row - 1][col] = color
            count += 1
    if x != 7:
        if arr[row + 1][col] != color:
            arr[row + 1][col] = color
            count += 1
    if y != 0:
        if arr[row][col - 1] != color:
            arr[row][col - 1] = color
            count += 1
    if y != 7:
        if arr[row][col + 1] != color:
            arr[row][col + 1] = color
            count += 1
    return count

def check_board(arr, i, j):
    count = 0
    for x in range(8):
        for y in range(8):
            count += check_cell(arr, i, x, j, y)
    return count

n, m = map(int, input().split())
arr = []
result = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
board = copy.deepcopy(arr)
for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        if arr[i][j] != "W":
            white = 1
        arr[i][j] = "W"
        white += check_board(arr, i, j)
        arr = copy.deepcopy(board)

        black = 0
        if arr[i][j] != "B":
            black = 1
        arr[i][j] = "B"
        black += check_board(arr, i, j)
        arr = copy.deepcopy(board)
        result.append(min(white, black))
print(min(result))