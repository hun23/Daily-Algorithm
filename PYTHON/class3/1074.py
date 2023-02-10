N, r, c = map(int, input().split())
distance = 0
div = 2
while not (r == 0 and c == 0):
    if r % div != 0:
        distance += div * (r % div)
        r = r - r % div
    if c % div != 0:
        distance += (div // 2) ** 2
        c = c - c % div
    div *= 2

print(distance)
# 가장 가까운 r, c 가 2의 배수인 점으로 이동 및 거리계산
# 가장 가까운 r, c가 4의 배수인 점으로 이동 및 이전 이동점으로부터 거리계산
# r의 경우 div로 나눈 나머지 * div, c의 경우 div를 2로 나눈 값의 제곱
# 0,0에 도달한 경우 break
