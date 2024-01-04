from sys import stdin, stdout
input = stdin.readline
print = stdout.write

# def SOD(num):
#     ret = 0
#     for i in range(2, int(num**0.5) + 1):
#         quo, rem = divmod(num, i)
#         if rem == 0:
#             ret += i
#             if quo != i:
#                 ret += quo
#     return ret

n = int(input())
ans = 0
for i in range(2, n // 2 + 1):
    ans += (n // i - 1) * i
print(f"{ans%1_000_000}\n")