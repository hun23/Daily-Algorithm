from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, K = map(int, input().split())
dots = []
for n in range(N):
    dots.append(tuple(map(int, input().split())))
dots.sort()
println(dots)

for dot in dots:
    