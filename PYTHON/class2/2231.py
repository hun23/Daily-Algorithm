n = int(input())

_sum = 0
for num in range(n):
    _sum = num
    for c in str(num):
        _sum += int(c)
    if _sum == n:
        print(num)
        break
else:
    print(0)