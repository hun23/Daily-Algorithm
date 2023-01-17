import sys

def is_prime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
count = 0
for num in arr:
    if is_prime(num):
        count += 1
print(count)