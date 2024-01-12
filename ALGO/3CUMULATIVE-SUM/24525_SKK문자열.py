from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


skk = input().strip()
cnts = [0]
prefix_sum = [0]
cnt = 0
for c in skk:
    cnt += 1
    if c in "KS":
        cnts.append(cnts[-1] + cnt)
        cnt = 0
        prefix_sum.append(prefix_sum[-1] + (2 if c == "S" else -1))
cnts.append(cnts[-1] + cnt + 1)

println(cnts)
println(prefix_sum)

ans = -1
for i in range(1, len(prefix_sum)):
    for j in range(i + 1, len(prefix_sum)):
        if prefix_sum[j] - prefix_sum[i - 1] == 0:
            temp = (cnts[j + 1] - 1) - cnts[i - 1]
            # println(f"i:{i}, j:{j}, temp:{temp}")
            if temp > ans:
                ans = temp
println(ans)
