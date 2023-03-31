N = int(input())
meetings = []
for n in range(N):
    meetings.append(tuple(map(int, input().split())))
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for n in range(N):
    start = meetings[n][0]
    if end <= start:
        cnt += 1
        end = meetings[n][1]
print(cnt)
