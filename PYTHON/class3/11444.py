from collections import deque
import time


def recursive(n, div):
    if n <= 1:
        return 1
    if n % 2 == 0:
        ret = (
            recursive(n // 2, div) ** 2
            + recursive(n // 2 - 1, div) ** 2
        )
        ret %= div
        return ret
    else:
        ret = recursive(n // 2, div) ** 2 + 2 * recursive(
            n // 2, div
        ) * recursive(n // 2 - 1, div)
        ret %= div
        return ret


# n = int(input())
# for n in range(10000):
n = 4
st = time.time()
div = 1000000007
temp = deque([1, 1])
if n <= 1:
    print(temp[n])
while_st = time.time()
i = 1
while i < n:
    t = temp.popleft()
    temp.append((t + temp[0]) % div)
    # temp.append((t + temp[0]))
    i += 1
while_end = time.time()
ret = recursive(n, div)
ret_end = time.time()
print(f"while: {temp[1]} / time: {while_end - while_st}")
print(f"recur: {ret} / time: {ret_end - while_end}")
# print(
#     f"ratio: {(while_end - while_st) / (ret_end - while_end) * 100}"
# )
