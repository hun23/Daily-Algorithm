N = int(input())
papers = [tuple(map(int, input().split())) for _ in range(N)]
big_paper = [[0 for _ in range(100)] for _ in range(100)]

for x_start, y_start in papers:
    for x in range(x_start, x_start + 10):
        big_paper[x][y_start : y_start + 10] = [1] * 10

ans = 0
for p in big_paper:
    ans += sum(p)
print(ans)