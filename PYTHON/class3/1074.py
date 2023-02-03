N, r, c =map(int, input().split())
# r행 c열
# n = 2일때 아래 칸으로 가면 2^n+1이 들어간다
# n = 3일때 2^n+1이 들어간다
# 3, 0 -> 2^n+1, 홀수면 +1
# 4, 0

# ar = 0
# ac = 0
# (3, 1)
# ar = (r // 2) * 2**(N + 1)
# ar +=
# # r % 2 == 1 & c % 2 == 0
# ar += 2
# # r % 2 == 0 & c % 2 == 1
# ar += 1
# # r % 2 == 1 & c % 2 == 1
# ar += 3

# c // 2 * 4
# answer = 0
# answer += (r // 2) * (2**(N + 1))
# answer += (c // 2) * 4
# if r % 2 == 1:
#     if c % 2 == 0:
#         answer += 2
#     else:
#         answer += 3
# else:
#     if c % 2 == 1:
#         answer += 1
# print(answer)
if r == 0 and c == 0:
    print(0)
    exit()

max_len = max(r, c)
binary = []
while max_len > 0:
    binary.append(str(max_len % 2))
    max_len //= 2
binary.reverse()
b = "".join(binary)
print(b)