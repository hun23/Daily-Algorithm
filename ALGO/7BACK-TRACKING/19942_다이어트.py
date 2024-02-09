from sys import stdin, stdout

input = stdin.readline

def println(s):
    stdout.write(f"{s}\n")

def compare(bin1, bin2):
    bin1_str = bin(bin1)[2:][::-1]
    bin2_str = bin(bin2)[2:][::-1]
    limit = min(len(bin1_str), len(bin2_str))
    for i in range(limit):
        if bin1_str[i] > bin2_str[i]:
            return bin1
        if bin1_str[i] < bin2_str[i]:
            return bin2
    return bin1 if bin1 < bin2 else bin2

N = int(input())
checklist = list(map(int, input().split()))
nutritions = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 10000]
for binary in range(1, 1 << N):
    temp = [0] * 5
    for n in range(N):
        # check if selected
        if not binary & (1 << n):
            continue
        # add all selected nutritions
        for i in range(5):
            temp[i] += nutritions[n][i]
        # check
        good = True
        for i in range(4):
            if checklist[i] > temp[i]:
                good = False
                break
        if good:
            if temp[4] < ans[1]:
                ans = [binary, temp[4]]
            elif temp[4] == ans[1]:
                ans[0] = compare(binary, ans[0])
if ans[1] == 10000:
    print(-1)
    exit()
print(ans[1])
first = True
for n in range(N):
    if ans[0] & (1 << n):
        if not first:
            print(f" {n + 1}", end="")
        else:
            print(n + 1, end="")
            first = False
