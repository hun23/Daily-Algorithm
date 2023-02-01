T = int(input()) # 테스트 케이스 수 입력
for tc in range(T): # 테스트 케이스 반복
    N = int(input())
    inp = list(map(int, input().split())) # 입력
    mx = 0 # 가능한 최소수(=1) - 1
    mn = 1000001 # 가능한 최대수(=1000000) + 1
    for num in inp:
        if num > mx:
            mx = num
        if num < mn:
            mn = num
    print(f"#{tc + 1} {mx - mn}")
