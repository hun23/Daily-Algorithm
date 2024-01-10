from sys import stdin, stdout
input = stdin.readline
inputs = map(int, input().split())
print = stdout.write

def println(s):
    print(f"{s}\n")

def get_GCD(n, m):
    while n % m != 0:
        temp = n % m
        n = m
        m = temp
    return m

N, M, K = inputs
dots = [(x, y) for x in range(N + 1) for y in range(M + 1)]
# println(dots)
ans = 0
for i in range(len(dots) - 1):
    x1, y1 = dots[i]
    for j in range(i + 1, len(dots)):
        x2, y2 = dots[j]
        # println(f"dots: {x1}.{y1} / {x2}.{y2}")
        cnt = 0
        if x2 - x1 == 0 or y2 - y1 == 0:
            cnt += abs(x2 - x1) + abs(y2 - y1) + 1
        else:
            cnt += (1 + get_GCD(abs(x2 - x1), abs(y2 - y1)))
        # println(f"cnt:{cnt}")
        if cnt == K:
            ans += 1
println(f"{ans}")
