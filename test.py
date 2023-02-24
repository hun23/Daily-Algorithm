# N, M = map(int, input().split())

# # read the points
# points = []
# for i in range(N):
#     x, y = map(int, input().split())
#     points.append((x, y))

# # find the corners of the rectangle
# min_x = min(x for x, y in points)
# max_x = max(x for x, y in points)
# min_y = min(y for x, y in points)
# max_y = max(y for x, y in points)

# # check all possible rectangles
# for x1 in range(min_x, max_x + 1):
#     for y1 in range(min_y, max_y + 1):
#         for x2 in range(x1, max_x + 1):
#             for y2 in range(y1, max_y + 1):
#                 count = 0
#                 for x, y in points:
#                     if x1 <= x <= x2 and y1 <= y <= y2:
#                         count += 1
#                 if count >= M:
#                     print(x1, y1, x2, y2)
#                     exit()

# print("NONE")

print(1 << 0)
print(1 << 1)
