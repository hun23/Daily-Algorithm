from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


"""
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25

N = 5
2 * 1, 2, 3, 4, 5
3 * 1, 2, 3, 4, 5
4 * 1, 2, 3, 4, 5
5 * 1, 2, 3, 4, 5

1
2 2
3 3
4 4 4
5 5
6 6
8 8
9
10 10
12 12
15 15
16
20 20
25

1
2 2
3 3
4
6 6
9
"""


def cnt_less_or_equal(num):
    global N, K
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, num // i)
    return cnt


N = int(input())
K = int(input())
left, right = 0, N * N
while left <= right:
    mid = (left + right) // 2
    if cnt_less_or_equal(mid) >= K:
        right = mid - 1
    else:
        left = mid + 1
println(left)
