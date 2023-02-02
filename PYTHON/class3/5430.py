import sys

# import time
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # parsing
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    inp = sys.stdin.readline().rstrip()
    # st = time.time()
    # arr = [0] * n
    # for i in range(n):
    #     arr[i] = inp[1 + i * 2]
    if n == 0:
        arr = deque()
    else:
        arr = deque([0] * n)
        for i in range(n):
            arr[i] = inp[1 + i * 2]

    # new
    error = False
    is_reversed = False
    for c in p:
        if c == "R":
            is_reversed = not is_reversed
        else:
            try:
                if is_reversed:
                    # arr = arr[:-1]
                    arr.pop()
                else:
                    # arr = arr[1:]
                    arr.popleft()
            except:
                error = True
                break
    if is_reversed:
        # arr = arr[::-1]
        arr.reverse()
    if error:
        print("error")
    else:
        print("[", end="")
        print(",".join(arr), end="")
        print("]")
    # ed = time.time()
    # print(ed - st)
    # do 시간초과
    # error = False
    # i = 0
    # while i < len(p):
    #     c = p[i]
    #     if c == "R":
    #         if i + 1 != len(p) and p[i + 1] == "R":
    #             i += 1
    #         else:
    #             arr.reverse()
    #     else:
    #         try:
    #             arr.popleft()
    #         except:
    #             error = True
    #             break
    #     i += 1
