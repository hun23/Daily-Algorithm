from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N, A = map(int, input().split())
ans = 0
degree = 1
while A ** degree <= N:
    ans += N // (A ** degree)
    degree += 1
print(f"{ans}\n")
