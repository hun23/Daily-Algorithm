def solve(m, comb, used):
    global N, M, arr, answers
    if m == M:
        answers.append(comb[:])
        return
    for n in range(N):
        if used & (1<<n):
            continue
        comb[m] = arr[n]
        solve(m + 1, comb, used | (1<<n))
    return

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answers = []
solve(0, [0] * M, 0)
answers.sort()
temp = None
for a in answers:
    if temp is None:
        print(*a)
        temp = a
    elif temp != a:
        print(*a)
        temp = a