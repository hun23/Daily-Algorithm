from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def println(s):
    print(f"{s}\n")

N = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0] * N
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = max(prefix_sum[i - 1] + arr[i], arr[i])
# println(prefix_sum)
println(max(prefix_sum))