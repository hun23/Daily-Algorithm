def move_till_block():
    pass  # return none if blackhole or start point


def blocks(block_num):
    if block_num <= 5:
        pass
    elif 6 <= block_num <= 10:
        pass
    elif block_num == -1:
        pass
    return


def is_reflected():
    pass


def go(arr, r, c):
    start = (r, c)
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):  # 4방향
        while True:
            block_num = move_till_block()
            if block_num is None:
                break
            d = blocks(block_num)
    pass


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            temp = go(arr, r, c)
            if temp > answer:
                answer = temp
    print(f"#{tc} {answer}")
