def check_side(ladder, row, col):
    # direction == -1: 왼쪽, +1: 오른쪽
    for direction in range(-1, 2):
        if direction == 0:
            continue
        side_col = col + direction
        if 100 > side_col >= 0:  # 옆이 인덱스 범위 내에 있고
            if ladder[row][side_col] == 1:  # 갈 수 있으면
                return direction  # 해당 방향 리턴
    return 0


def can_go_forward(ladder, row, col):
    forward_row = row - 1  # 한 줄 앞으로
    if 100 > forward_row >= 0:  # 인덱스 범위 내에 있고
        if ladder[forward_row][col] == 1:  # 길이 있으면
            return True
    return False


# f = open("./Python/im/from_notion/1210.txt", "r")
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # tc = int(f.readline())
    # ladder = [
    #     list(map(int, f.readline().split())) for _ in range(100)
    # ]
    row, col = 99, ladder[-1].index(2)  # 시작점
    while row != 0:
        direction = check_side(ladder, row, col)  # 옆길 확인
        if direction:  # 옆에 길이 있으면, -1: 왼쪽, +1: 오른쪽
            col += direction  # 일단 옆으로
            while not can_go_forward(ladder, row, col):  # 앞으로 갈 수 없으면
                col += direction  # 옆으로
            row -= 1  # 앞으로 갈 수 있게 되면 한칸 앞으로
        else:  # 옆에 길이 없으면
            row -= 1  # 앞으로
    print(f"#{tc} {col}")
