from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for m in range(1, M + 1):
        prefix_sum[n][m] = (
            arr[n - 1][m - 1]
            + prefix_sum[n - 1][m]
            + prefix_sum[n][m - 1]
            - prefix_sum[n - 1][m - 1]
        )

ans = -(200 * 200 * 10000)
for n1 in range(1, N + 1):
    for m1 in range(1, M + 1):
        for n2 in range(n1, N + 1):
            for m2 in range(m1, M + 1):
                temp = (
                    prefix_sum[n2][m2]
                    - prefix_sum[n2][m1 - 1]
                    - prefix_sum[n1 - 1][m2]
                    + prefix_sum[n1 - 1][m1 - 1]
                )
                if ans < temp:
                    ans = temp
println(ans)
##########################################################
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
matrix = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]


MAX = float('-inf')
for i in range(1, N+1):
    row = [0] * (M + 1)
    # i행부터 각 열끼리의 누적합 저장
    for j in range(i, N+1):
        col = [0] * M
        # row로 구한 누적합을 부분합하여 최댓값을 저장
        for k in range(1, M+1):
            row[k] += matrix[j][k]
            # i행부터 j행까지 k열의 누적합
            col[k-1] = max(col[k-2] + row[k], row[k])
            # i행 ~ j행까지 열끼리의 누적합 중에서 k열까지 부분합의 최대값 갱신
        temp = max(col)
        if temp > MAX:
            MAX = temp

print(MAX)
