from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())
ans = 1
while ans * ans <= N:
    ans += 1
print(f"{ans - 1}\n")
