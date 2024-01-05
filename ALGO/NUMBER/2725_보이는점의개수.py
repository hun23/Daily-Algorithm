from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def GCD(n, m):
    while n % m != 0:
        temp = n % m
        n = m
        m = temp
    return m

ans = [0] * 1001
for n in range(2, 1001):
    temp = 0
    for i in range(1, n):
        if GCD(i, n) == 1:
            temp += 1
    ans[n] = ans[n - 1] + temp

C = int(input())
for c in range(C):
    N = int(input())
    print(f"{ans[N] * 2 + 3}\n")
