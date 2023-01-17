n = int(input())
circle = 0
plus = 1
count = 0
while (1 + 6 * circle < n):
    circle += plus
    plus += 1
    count += 1
print(count + 1)
# 1 ~ 1 + 6 * 0
# 2 ~ 1 + 6 * 1
# 8 ~ 1 + 6 * 3
# 20 ~ 1 + 6 * 6
# 38 ~ 1 + 6 * 10