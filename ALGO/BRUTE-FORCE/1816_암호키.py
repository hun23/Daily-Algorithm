N = int(input())
numbers = [int(input()) for _ in range(N)]

for num in numbers:
    is_good = 0
    for i in range(2, 1_000_000 + 1):
        if num % i == 0:
            is_good = 1
            break
    print(["YES", "NO"][is_good])
