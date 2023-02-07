N = int(input())
area = set()
for n in range(N):
    x, y = map(int, input().split())
    for r in range(10):
        for c in range(10):
            area.add((x + c, y + r))
print(len(area))
