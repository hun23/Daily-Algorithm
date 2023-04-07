def get_power_set(start, end, ps):
    global N, arr
    for i in range(1 << (end - start)):
        ret = 0
        for j in range(len(str(bin(end-start))) - 2):
            if i & (1 << j):
               ret += arr[start + j]
        if ps.get(ret) is None:
            ps[ret] = 1
        else:
            ps[ret] += 1
    return ps


def solve(left, right):
    global S
    mid = (left + right) // 2
    left_power_set, right_power_set = dict(), dict()
    left_power_set[S], right_power_set[S] = 0, 0
    left_power_set = get_power_set(0, mid, left_power_set)
    right_power_set = get_power_set(mid + 1, right, right_power_set)

    answer = left_power_set[S] + right_power_set[S]
    for le in left_power_set.keys():
        for ri in right_power_set.keys():
            if le + ri == S:
                answer += 1
    return answer


N, S = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(0, N))
