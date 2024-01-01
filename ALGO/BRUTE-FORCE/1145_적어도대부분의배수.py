numbers = list(map(int, input().split()))

for n in range(1, 100 ** 5 + 1):
    cnt = 0
    for num in numbers:
        if n % num == 0:
            cnt += 1
            if cnt >= 3:
                print(n)
                exit()
