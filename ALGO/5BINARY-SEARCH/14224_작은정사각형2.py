from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def possible(num):
    global dots, K
    for xdot in dots:
        for ydot in dots:
            # 왼쪽 위 점을 시작으로 정사각형 그리기
            x, y = xdot[0] - 1, ydot[1] + 1
            # println(f"x:{x} y:{y}")
            # 안에 점이 몇개인지 세고
            cnt = 0
            for xtemp, ytemp in dots:
                if x < xtemp < x + num and y - num < ytemp < y:
                    cnt += 1
                    if cnt >= K:
                        return True
                # println(f"xtemp:{xtemp}, ytemp:{ytemp}, cnt:{cnt}, num: {num}")
    return False


N, K = map(int, input().split())
dots = []
for n in range(N):
    dots.append(tuple(map(int, input().split())))
dots.sort()

left, right = 1, 2_000_000_000 + 2
while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        right = mid - 1
    else:
        left = mid + 1
println(left**2)
