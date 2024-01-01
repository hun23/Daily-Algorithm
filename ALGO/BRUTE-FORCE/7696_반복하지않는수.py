# 한자리
# 1 ~ 9

# 두자리
# 10, 12, 13, 14, 15, 16, 17, 18, 19
# 9 * 9

# 세자리
# 9C1 9C1 8C1
# 9 * 9 * 8

def no_rep(n):
    check = [False] * 10
    while n > 0:
        if check[n % 10]:
            return False
        check[n % 10] = True
        n //= 10
    return True

# 각 자리수 까지의 반복X수 개수
limit_list = [0]
limit = 9
cnt = 1
while limit <= 2_000_000:
    limit_list.append(limit + limit_list[cnt - 1])
    limit *= (10 - cnt)
    cnt += 1

N = int(input())
while N != 0:
    length, diff = 0, 0
    for i, limit in enumerate(limit_list):
        if N <= limit:
            length = i
            diff = N - limit_list[i - 1]
            break
    # length 자리수 중 diff 번째 숫자
    num, cnt = 10 ** (length - 1) - 1, 0
    print(length, diff, num)
    
    # diff 를 9로 나눈 몫 + 1 = 처음 자리수
    # 반복
    answer = [0] * 10
    temp = 1
    for i in range(length - 1):
        temp *= (9 - i)
    answer[10 - length] = diff // temp + 1
    diff = diff % temp
    
    while cnt != diff:
        num += 1
        if no_rep(num):
            cnt += 1
        # if cnt < 30 or diff - cnt < 30:
        #     print(num, cnt)
    print(num)
    N = int(input())