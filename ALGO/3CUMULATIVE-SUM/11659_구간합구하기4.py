from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def println(s):
    print(f"{s}\n")

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
prefix_sum[1] = numbers[0]
for i in range(2, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

for m in range(M):
    i, j = map(int, input().split())
    println(f"{prefix_sum[j] - prefix_sum[i - 1]}")
