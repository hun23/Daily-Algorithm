import sys


def get_max(pillars, start_idx, end_idx):
    return sorted(pillars[start_idx:end_idx], key=lambda x: x[1])[-1][1]


n = int(input())
pillars = []
for _ in range(n):
    location, height = map(int, sys.stdin.readline().rstrip().split())
    pillars.append((location, height))
pillars.sort(key=lambda x: x[0])
# print(pillars)
# 오목하면 안된다 = 높이가 작아졌다가 커지면 안된다
# 다시 말해, 최대 높이가 아닌 기둥을 제외하고는 지붕 높이가 낮아지면 안된다
# 다시 말해, 최대 높이 기둥을 지나면 남은 기둥 중 최대높이만큼만 작아져야 한다.
# 가장 왼쪽 기둥높이를 최소높이로 시작해서
# 더 큰걸 만나면 높이고

# 왼쪽부터 시작해서
# 다음 기둥이 더 크면 -> 그만큼 높이고
# 다음 기둥이 더 작으면 -> 현재 기둥이 최대 높이면 다음 기둥만큼 내림 아니면 통과
# 최대 높이 통과시
# 남은 최대 높이 기둥까지는 해당 높이로
# 지나고는 계속 반복

# area = 0
# current_location = pillars[0][0]
# current_height = pillars[0][1]
# for (i, p) in enumerate(pillars[1:]):
#     pillar_lo = p[0]
#     pillar_h = p[1]
#     if current_height < pillar_h:
#         area += current_height * (pillar_lo - current_location)
#         current_height = pillar_h
#         current_location = pillar_lo
#     elif current_height > pillar_h:  # 같을경우 무시함에 주의
#         if pillar_h == get_max(pillars, i):
#             area += pillar_h * (pillar_lo - current_location)
#             current_location = pillar_lo
# print(area + get_max(pillars, 0))

max_h = get_max(pillars, 0, len(pillars))
max_width = pillars[0][0] - pillars[-1][0] + 1
area = 0
while True:
    start_lo = 0
    start_idx = 0
    end_lo = 0
    end_idx = 0
    for (i, p) in enumerate(pillars):
        if p[1] == max_h:
            if start_lo == 0:
                start_lo = p[0]
                start_idx = i
            end_lo = p[0]
            end_idx = i
    area += max_h * (end_lo - start_lo + 1)
    max_h = max(get_max(pillars, 0, start_idx), get_max(pillars, end_idx + 1, len(pillars)))
# 넓이 구하고 지워버리면 될 듯!
for h in range(max_h, 0, -1):

