N, M = map(int, input().split())
temp = 1
for n in range(N, N - M, -1):
    temp *= n
# print(temp)
for m in range(1, M + 1):
    temp //= m
print(temp)
