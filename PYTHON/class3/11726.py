N = int(input())
# dp값 저장 위한 딕셔너리
d = {key: 0 for key in range(1, N + 1)}
# 초기값 설정
d[1] = 1
d[2] = 2
for n in range(3, N + 1):
    if d[n] != 0:
        continue  # 값이 이미 있으면 통과
    # dn = 맨 앞이 세로로 있는 경우(나머지 칸(n-1)을 채우는 경우의 수)
    # 더하기 맨 앞이 두칸 누워있는 경우(나머지 칸(n-2)를 채우는 경우의 수)
    d[n] = (d[n - 1] + d[n - 2]) % 10007  # 나머지만 저장해도 무방
print(d[N])
