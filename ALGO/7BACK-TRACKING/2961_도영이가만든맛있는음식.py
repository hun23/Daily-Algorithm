from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")

def recur(idx, sour, bitter):
    global N
    if idx == N:
        if sour == 1 and bitter == 0:
            return 2147483647
        return abs(sour - bitter)
    s, b = ingredients[idx]
    return min(
        recur(idx + 1, sour * s, bitter + b),
        recur(idx + 1, sour, bitter)
    )

N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]
println(recur(0, 1, 0))
