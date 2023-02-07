N = int(input())
fives = [f for f in range(0, N + 1 + 5, 5)]
ffives = [f for f in range(0, N + 1 + 25, 25)]
fffives = [f for f in range(0, N + 1 + 125, 125)]
answer = 0

i = 0
while fives[i] <= N:
    i += 1
answer += i - 1

i = 0
while ffives[i] <= N:
    i += 1
answer += i - 1

i = 0
while fffives[i] <= N:
    i += 1
answer += i - 1
print(answer)

# fac = 1
# for i in range(1, N + 1):
#     fac *= i
# cnt = 0
# while True:
#     if fac % 10 == 0:
#         cnt += 1
#     else:
#         break
#     fac //= 10
# print(cnt)
