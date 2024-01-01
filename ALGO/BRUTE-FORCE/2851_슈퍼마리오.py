points = [int(input()) for _ in range(10)]
ans = 0

total = 0
for p in points:
    total += p
    if abs(ans - 100) >= abs(total - 100):
        ans = total
print(ans)