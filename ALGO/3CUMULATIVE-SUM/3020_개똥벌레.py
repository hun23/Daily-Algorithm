from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, H = map(int, input().split())
cnts = [0] * H
for n in range(N):
    h = int(input().strip())
    if n % 2 == 0:
        cnts[0] += 1
        cnts[h] -= 1
    else:
        cnts[H - h] += 1

ans, ans_cnt = 2147483647, 0
for i in range(len(cnts)):
    if i != 0:
        cnts[i] += cnts[i - 1]
    if ans > cnts[i]:
        ans = cnts[i]
        ans_cnt = 1
    elif ans == cnts[i]:
        ans_cnt += 1
println(f"{ans} {ans_cnt}")
