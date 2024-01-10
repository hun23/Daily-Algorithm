from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def println(s):
    print(f"{s}\n")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
prefix_sum = [0] * N
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for i in range(N):
    for j in range(i, -1, -1):
        if i == j:
            temp = prefix_sum[i]
        else:
            temp = prefix_sum[i] - prefix_sum[j]
        # println(f"i:{i} / j:{j} / temp: {temp}")
        if temp == K:
            ans += 1
println(ans)
