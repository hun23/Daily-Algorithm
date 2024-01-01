N = int(input())
ans = 0

for B in range(1, 501):
    for A in range(B, 501):
        if A * A - B * B == N:
            ans += 1
print(ans)