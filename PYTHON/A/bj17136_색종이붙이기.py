def get_coordinate(arr, co):
    start = co[0] * 10 + co[1]
    one_line = sum(arr, [])
    for idx in range(start, 10 * 10):
        if one_line[idx] == 1:
            return idx//10, idx%10
    return None

def recursion(arr, paper_count, prev_coordinate):
    global answer, answer_list
    coordinate = get_coordinate(arr, prev_coordinate)
    if coordinate is None:  # when filled all 1s
        if answer > 25 - sum(paper_count):
            answer = 25 - sum(paper_count)
            answer_list = paper_count[:]
        return
    elif sum(paper_count) == 0:  # when all papers are used
        return

    # check possible max paper length at the coordinate
    r, c = coordinate
    length = 0
    while arr[r + length][c] == 1 and arr[r][c + length] == 1:  # need to check diagonally
        length += 1
        if r + length >= 10 or c + length >= 10 or length >= 5:
            break
    for len_ in range(length, 0, -1):
        if paper_count[len_] == 0:
            continue
        # change arr
        for i in range(len_):
            for j in range(len_):
                arr[r + i][c + j] = 0
        # change paper_count
        paper_count[len_] -= 1

        # recursion
        recursion(arr, paper_count, coordinate)

        # reset arr changes
        for i in range(len_):
            for j in range(len_):
                arr[r + i][c + j] = 1
        # change paper_count
        paper_count[len_] += 1


arr = [list(map(int, input().split())) for _ in range(10)]
paper_count = [0, 5, 5, 5, 5, 5]
answer = 2147483647
answer_list = []
recursion(arr, paper_count, (0, 0))
if answer == 2147483647:
    print(-1)
else:
    print(answer)
print(answer_list)
