T = int(input())
# 피보나치 수열 key(=순서) : value(0횟수, 1횟수)
fibo = {key: [0, 0] for key in range(41)}
fibo[0] = [1, 0]
fibo[1] = [0, 1]
for tc in range(T):
    N = int(input())
    # 값이 이미 있으면
    if fibo.get(N) != [0, 0]:
        print(*fibo[N], sep=" ")  # 출력
        continue
    #  값이 없으면
    i = 2
    while i <= N:
        if fibo[i] == [0, 0]:  # 값이 없는 경우에는
            for j in range(2):  # 계산
                fibo[i][j] = fibo[i - 2][j] + fibo[i - 1][j]
        i += 1
    print(*fibo[N], sep=" ")
