A, B = map(int, input().split())
ans = []

for x in range(-10000, 10000):
    if x * x + 2 * A * x + B == 0:
        ans.append(x)
print(*ans)