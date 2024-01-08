from sys import stdin, stdout
input = stdin.readline
inputs = map(int, input().split())
print = stdout.write

def println(s):
    print(f"{s}\n")

N, M, K = inputs
dots = [(x, y) for x in range(N + 1) for y in range(M + 1)]
# println(dots)
ans = 0
for i in range(len(dots) - 1):
    x1, y1 = dots[i]
    for j in range(i + 1, len(dots)):
        x2, y2 = dots[j]
        cnt = 2
        if x2 - x1 == 0:
            cnt += y2 - y1 - 1
        else:
            slope = (y2 - y1) / (x2 - x1)
            new_x, new_y = x1 + 1, y1 + slope
            # println(f"dot1: {x1}/{y1}, dot2: {x2}/{y2}, slope: {slope}")
            while new_x != x2 or new_y != y2:
                # println(f"new: {new_x}/{new_y}")
                if int(new_x) == new_x and int(new_y) == new_y:
                    cnt += 1
                new_x += 1
                new_y += slope
            # println(f"cnt: {cnt}")
        if cnt == K:
            ans += 1
println(f"{ans}")