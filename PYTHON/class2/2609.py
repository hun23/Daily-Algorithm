#최대공약수 & 최소공배수 구하기
a, b = map(int,input().split())

# a, b 약수 구하기
def get_yaksu(num):
    ret = set()
    for i in range(1, num + 1):
        if num % i == 0:
            ret.add(i)
    return ret

a_yaksu = get_yaksu(a)
b_yaksu = get_yaksu(b)

# a, b 약수 set에서 교집합 중 최대 = 최대공약수
gongyaksu = max((a_yaksu & b_yaksu))
print(gongyaksu)
# a * b = 최대공약수 * 최소공배수 -> a * b / 최대공약수 = 최소공배수
print(int(a * b / gongyaksu))