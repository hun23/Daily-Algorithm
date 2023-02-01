import sys

# 입력
n = int(sys.stdin.readline().rstrip())
color_papers = [
    tuple(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(n)
]
mp = [[0 for _ in range(1001)] for _ in range(1001)]

# 색종이 하나씩 놓기
# min lx, min ly, max hx, max hy
limits = [1000, 1000, 0, 0]
for (i, cp) in enumerate(color_papers):
    # lx, ly, hx, hy
    co = [cp[0], cp[1], cp[0] + cp[2], cp[1] + cp[3]]
    for x in range(co[0], co[2]):
        for y in range(co[1], co[3]):
            mp[x][y] = i + 1  # 지도(mp)의 값을 색종이 번호(1번~)로 바꿈
    for j in range(4):
        if j < 2:
            limits[j] = min(co[j], limits[j])
        else:
            limits[j] = max(co[j], limits[j])

# 지도 순회하며 개수세기
# 색종이별 개수 카운트 위한 딕셔너리
answer = {i + 1: 0 for i in range(len(color_papers))}
for x in range(limits[0], limits[2]):
    for y in range(limits[1], limits[3]):
        v = mp[x][y]
        if v:  # 해당 칸의 값이 0이 아니면
            answer[v] += 1  # 색종이별 칸 개수 추가
print("\n".join(map(str, answer.values())))
