def to_arr(s):
    arr = []
    for c in s:
        arr.append(ord(c) - 96)
    return arr


def func(arr, m, p):
    sum = 0
    # arr 순회하며 더하기
    for (idx, a) in enumerate(arr):
        sum += calc(a, idx, m, p)
        if sum > m:  # sum이 m보다 커지면 -> 몫을 남길필요X
            sum %= m  # 나머지만 남김
    return sum


def calc(a, idx, m, p):
    val = a
    for i in range(idx):
        val *= p
        if val > m:  # val이 m보다 커지면 -> 몫을 남길필요X
            val %= m  # 나머지만 남김
    return val


n = int(input())
s = input()
# 입력을 나눌 큰 소수
m = 1234567891
# 입력에 곱할 소수
p = 31
# 입력 알파벳을 숫자로
arr = to_arr(s.lower())
# 계산
answer = func(arr, m, p)
print(answer)
