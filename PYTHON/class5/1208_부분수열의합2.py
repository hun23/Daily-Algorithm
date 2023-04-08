def get_power_set(start, end, ps):
    global N, arr
    for i in range(1, 1 << (end - start + 1)):
        ret = 0
        for j in range(end - start + 1):
            if i & (1 << j):
                ret += arr[start + j]
            j += 1
        if ps.get(ret) is None:
            ps[ret] = 1
        else:
            ps[ret] += 1
    return ps


def solve(left, right):
    global S
    mid = (left + right) // 2
    left_power_set, right_power_set = dict(), dict()
    left_power_set = get_power_set(0, mid, left_power_set)
    right_power_set = get_power_set(mid + 1, right, right_power_set)
    # print(left_power_set)
    # print(right_power_set)
    answer = 0
    if left_power_set.get(S) is not None:
        answer += left_power_set[S]
    if right_power_set.get(S) is not None:
        answer += right_power_set[S]
    lkeys = sorted(list(left_power_set.keys()))
    rkeys = sorted(list(right_power_set.keys()))
    lptr, rptr = 0, len(rkeys) - 1
    while lptr < len(lkeys) and 0 <= rptr:
        value = lkeys[lptr] + rkeys[rptr]
        if value < S:
            lptr += 1
        elif value > S:
            rptr -= 1
        else:
            answer += left_power_set[lkeys[lptr]] * right_power_set[rkeys[rptr]]
            rptr -= 1
            lptr += 1
    return answer


N, S = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(0, N - 1))
