# math
n = int(input())
answer = 0  # 자루개수
while n > 0:
    f_quo, f_rem = divmod(n, 5)
    if f_rem == 0:  # 5로 나눈 나머지가 0이면
        answer += f_quo  # 몫만큼 개수에 더한다
        n = 0  # n = 0으로 맞추어 print시 조건 만족하도록
        break
    n -= 3  # 5의 배수가 아니면
    answer += 1  # n에서 3개(=1자루) 빼고 그만큼 답에 추가
print(answer if n == 0 else -1)  # n != 0이면 5, 3의 배수로 나눌수 없으므로
