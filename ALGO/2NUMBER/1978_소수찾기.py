from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def is_prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

N = int(input())
numbers = list(map(int, input().split()))

ans = 0
for num in numbers:
    ans += is_prime(num)
print(f"{ans}")