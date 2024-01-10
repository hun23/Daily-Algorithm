A, B = map(int, input().split())
# B 까지의 2**degree의 개수(=B//div) - (A-1) 까지의 2**degree의 개수(=(A-1)//div)를
# 이전 차수(2**(degree-1))와의 차이 만큼 ans에 추가(=2**degree-2**(degree-1))
degree = 1
ans = B - A + 1  # 홀수인 경우
while 2**degree <= B:
    ans += (B // (2**degree) - (A - 1) // (2**degree)) * ((2**degree) - 2 ** (degree - 1))
    degree += 1
print(ans)