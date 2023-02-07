N = int(input())
# 인접행렬을 그래프로 변환
graph = {key: [] for key in range(N)}
for n in range(N):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i]:
            graph[n].append(i)
# 정답 저장 배열
answers = [[0] * N for _ in range(N)]
# DFS
for i in range(N):
    can_visit = []  # 방문 리스트
    first = True  # 첫 방문인 경우
    stack = []
    stack.append(i)
    while stack:
        cur = stack.pop()
        if cur not in can_visit:
            if not first:  # 첫 방문이 아닌 경우에만 방문 리스트 추가
                can_visit.append(cur)
            else:
                first = False  # 첫 방문 flag 업데이트
            for nex in graph[cur]:
                stack.append(nex)
    for cv in can_visit:
        answers[i][cv] = 1
for a in answers:
    print(*a, sep=" ")
# print(answers)
# print(graph)
