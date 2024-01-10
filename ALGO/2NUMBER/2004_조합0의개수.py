from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def println(s):
    print(f"{s}\n")

def count_multiple(n, div):
    ret = 0
    degree = 1
    cnt = n // (div**degree)
    while cnt != 0:
        ret += cnt
        degree += 1
        cnt = n // (div**degree)
    return ret

N, M = map(int, input().split())

ans = min(
    count_multiple(N, 2) - (count_multiple(M, 2) + count_multiple(N - M, 2)),
    count_multiple(N, 5) - (count_multiple(M, 5) + count_multiple(N - M, 5))
)
println(f"{ans}")