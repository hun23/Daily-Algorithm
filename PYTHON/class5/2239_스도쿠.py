def get_valid_numbers(r, c):
    global arr
    possible = list(range(10))
    # check hor
    for i in range(9):
        possible[arr[r][i]] = 0
    # check ver
    for i in range(9):
        possible[arr[i][c]] = 0
    # check box
    r, c = r//3 * 3, c//3 * 3
    for i in range(9):
        possible[arr[r + i//3][c + i%3]] = 0
    return [p for p in possible if p != 0]


def solve(idx):
    global arr, zeros
    if idx == len(zeros):
        for a in arr:
            print(*a, sep="")
        exit(0)
        return
    r, c = zeros[idx]
    valid_numbers = get_valid_numbers(r, c)
    if len(valid_numbers) == 0:
        return
    for num in valid_numbers:
        arr[r][c] = num
        solve(idx + 1)
        arr[r][c] = 0
    return


arr = [list(map(int, list(input()))) for _ in range(9)]
zeros = [(r, c) for r in range(9) for c in range(9) if arr[r][c] == 0]
solve(0)
