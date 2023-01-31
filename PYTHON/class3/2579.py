n = int(input())
scores = [0 for _ in range(n + 2)]
scores[0] = 0  # 0번째 계단(시작점)은 0점짜리
for i in range(1, n + 1):
    scores[i] = int(input())
# 0번째 계단부터 n번째 계단까지 더한 값 저장 위한 리스트
d = [0 for _ in range(n + 1)]
d[1] = scores[1]  # 1번째 계단 더한 값은 1번째 계단 점수와 같으므로
if n >= 2:
    for i in range(2, n + 1):
        try:  # n == 2일때
            leap_n_step = scores[i] + scores[i - 1] + d[i - 3]
        except:  # 그 외
            leap_n_step = 0  # 이번칸에 2칸 뛰고(leap) 한칸 올라온(step) 경우
        leap = scores[i] + d[i - 2]  # 이번칸으로 2칸 뛴 경우
        d[i] = max(leap, leap_n_step)  # 둘 중 최대값 저장
print(d[n])
