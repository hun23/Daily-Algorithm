def get_coordinate(arr, co):
    start = co[0] * 10 + co[1]
    one_line = sum(arr, [])
    for idx in range(start, 10 * 10):
        if one_line[idx] == 1:
            return idx//10, idx%10
    return None

def recursion(arr, paper_count, prev_coordinate):
    global answer, answer_list
    coordinate = get_coordinate(arr, prev_coordinate)  # get next coordinate with 1
    used_paper_count = 25 - sum(paper_count)
    if coordinate is None:  # when filled with all 0s
        if answer > used_paper_count:
            answer = used_paper_count
            answer_list = paper_count[:]  # for debugging
        return
    elif sum(paper_count) == 0:  # when all papers are used
        return
    elif answer < used_paper_count:  # prunning
        return

    # check possible max paper length at the coordinate
    r, c = coordinate
    length = 1
    while length <= 5:
        stop = False
        for idx in range(length * length):
            # a, b = r + idx//length, c + idx%length
            if arr[r + idx//length][c + idx%length] == 0:
                stop = True
            if r + length > 10 or c + length > 10:
                stop = True
            if stop:
                break
        if stop:
            break
        length += 1
    length -= 1
    # print(length)
    # while arr[r + length][c] == 1 and arr[r][c + length] == 1:  # need to check diagonally
    #     length += 1
    #     if r + length >= 10 or c + length >= 10 or length >= 5:
    #         break
    # print(length)
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
paper_count = [0, 5, 5, 5, 5, 5]  # paper_count[1] -> count of paper size 1
answer = 2147483647
answer_list = []  # for debugging
recursion(arr, paper_count, (0, 0))
if answer == 2147483647:
    print(-1)
else:
    print(answer)
# print(answer_list)
