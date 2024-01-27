from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def new_dot(a, b):
    return (a[0] + b[0], a[1] + b[1])


N = int(input())
A, B = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(N)]
di = dict()
for dot in dots:
    di[dot] = True
ans = 0
for dot in dots:
    for nxt in [(A, 0), (A, B), (0, B)]:
        if not di.get(new_dot(dot, nxt), False):
            break
    else:
        ans += 1
println(ans)
