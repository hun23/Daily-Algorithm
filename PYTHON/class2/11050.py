n, k = map(int, input().split())

answer = 1
for i in range(n, 0, -1):
    # n ~ k+1까지 곱하고 = n!/k!
    if i > k:
        answer *= i
    # n - k ~ 1까지 나누고 = ~/(n - k)!
    if (n - k) >= i:
        answer /= i
print(int(answer))