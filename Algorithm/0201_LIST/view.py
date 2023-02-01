for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    for i in range(2, N - 2):
        h = buildings[i]
        small_but_tall = 0
        for j in range(1, 3): # 양쪽 체크
            left = buildings[i - j]
            right = buildings[i + j]
            small_but_tall = max([small_but_tall, left, right])
        if h > small_but_tall:
            count += h - small_but_tall
    print(f"#{tc} {count}")
