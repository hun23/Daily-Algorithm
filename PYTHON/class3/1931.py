N = int(input())
graph = dict()
mx = 0
for n in range(N):
    st, ed = map(int, input().split())
    if graph.get(st) == None:
        graph[st] = [ed]
    else:
        graph[st].append(ed)
    if ed > mx:
        mx = ed

# 인덱스로 만들어서 DFS?
# 값 범위가 너무 커서 메모리 폭발
# 그래프로 만들어야 할 듯.
# 회의가 있어도 스킵해야 할 경우?
# 회의가 바로 끝나는 경우?
distances = {key: 0 for key in graph.keys()}
mxcnt = 0
for key in sorted(graph.keys()):
    if len(graph[key]) == 0:
        continue
    stack = []
    stack.append(key)
    cnt = 0
    while stack:
        cur = stack.pop()
        # visited 판단 필요 없음, 어차피 앞으로만 간다
        # 바로 이어지는 회의 있는지 확인, 없으면 한칸 앞으로(cur += 1)
        while graph.get(cur) is None:
            cur += 1
            if cur >= mx:
                break
        if cur >= mx:  # 마지막 회의 끝나는 시간에 도달
            if mxcnt > cnt:
                mxcnt = cnt
            break
        for nex in graph[cur]:
            cnt += 1
            stack.append(nex)
print(mxcnt)
