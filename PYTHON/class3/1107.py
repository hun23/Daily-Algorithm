N = int(input())
M = int(input())
available = [True] * 10
broken = list(map(int, input().split()))
for b in broken:
    available[b] = False
current_channel = 100
digits = 0
n = N
while n > 0:
    n /= 10
    digits += 1
if N == 0:
    digits = 1
possible = []
# 자리수 + 1 에서 제일 작은 수
mn = 0
for i in range(digits + 1):
    if i == 0:
        for j in range(1, 10):
            if available[j]:
                mn += j * (10**digits)
                continue
        else:
            break
    else:
        for j in range(10):
            if available[j]:
                mn += j * (10 ** (digits - i - 1))
# 자리수 - 1 에서 제일 큰 수
# 같은 자리수 모든 경우
