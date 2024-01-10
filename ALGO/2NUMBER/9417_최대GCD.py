from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def get_GCD(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b

N = int(input())
for n in range(N):
    numbers = list(map(int, input().split()))
    ans = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            ans = max(ans, get_GCD(numbers[i], numbers[j]))
    print(f"{ans}\n")