from sys import stdin, stdout
input = stdin.readline
inputs = map(int, input().split())
print = stdout.write

def println(s):
    print(f"{s}\n")

def is_prime(num):
    if num <= 1 :
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

A, B, D = inputs
ans = 0
for num in range(A, B + 1):
    if is_prime(num):
        while num > 0:
            num, rem = divmod(num, 10)
            if rem == D:
                ans += 1
                break
println(f"{ans}")
