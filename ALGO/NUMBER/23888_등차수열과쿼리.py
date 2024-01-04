import sys

def get_sum(a, d, l, r):
    return a * (r - l + 1) + (r * (r - 1) - (l - 1) * (l - 2)) * d // 2

def GCD(n, m):
    while n % m != 0:
        temp = n % m
        n = m
        m = temp
    return m

def get_GCD(a, d, l, r):
    if d == 0:
        return a
    if l == r:
        return a + d * (r - 1)
    return GCD(a, d)

a, d = map(int, sys.stdin.readline().split())
q = int(sys.stdin.readline())
for _ in range(q):
    t, l, r = map(int, sys.stdin.readline().split())
    if t == 1:
        print(get_sum(a, d, l, r))
    else:
        print(get_GCD(a, d, l, r))
