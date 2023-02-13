w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

print((p + t) % w, (q + t) % h)

# dx = 1
# dy = 1

# used_t = 0
# d = 0
# nx, ny = p, q
# while t > 0:
#     nx = nx + dx
#     ny = ny + dy
#     # print(nx, ny)
#     if nx == 0 or nx == w:
#         dx *= -1
#     if ny == 0 or ny == h:
#         dy *= -1
#     t -= 1
#     used_t += 1
#     if (nx, ny) == (p, q):
#         while t > 0:
#             t -= used_t
#         t += used_t
# print(nx, ny)
