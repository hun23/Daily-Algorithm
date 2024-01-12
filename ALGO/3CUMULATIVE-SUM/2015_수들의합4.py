from collections import defaultdict
import random
from tqdm import tqdm

# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write

# def println(s):
#     print(f"{s}\n")

# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

# ans = 0
# prefix_sum = [0] * N
# prefix_sum[0] = arr[0]
# for i in range(1, N):
#     prefix_sum[i] = prefix_sum[i - 1] + arr[i]

# di = dict()
# for ps in prefix_sum:
#     ans += di.get(ps, 0)
#     di[ps + K] = di.get(ps + K, 0) + 1
# ans += di.get(K, 0)
# println(prefix_sum)
# println(di)
# println(ans)
# for i in range(N):
#     for j in range(i, -1, -1):
#         if i == j:
#             temp = prefix_sum[i]
#         else:
#             temp = prefix_sum[i] - prefix_sum[j]
#         # println(f"i:{i} / j:{j} / temp: {temp}")
#         if temp == K:
#             ans += 1
# println(ans)


def my(N, K, arr):
    ans = 0
    prefix_sum = [0] * N
    prefix_sum[0] = arr[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    di = dict()
    di[K] = 1
    for ps in prefix_sum:
        ans += di.get(ps, 0)
        di[ps + K] = di.get(ps + K, 0) + 1
    # ans += di.get(K, 0)
    # print(prefix_sum)
    # print(di)
    return ans


def answer(N, K, arr):
    S = [0]
    for i in range(N):
        S.append(S[-1] + arr[i])

    answer = 0
    idx_dict = defaultdict(list)
    for i in range(N, 0, -1):
        SUM = S[i]

        if SUM == K:
            answer += 1

        target = SUM + K
        answer += len(idx_dict[target])

        idx_dict[SUM].append(i)

    return answer


T = 10000
# 200_000, 2_000_000_000, 10_000
n_range = 200_000
k_range = 2_000_000_000
arr_range = 10_000
for t in tqdm(range(T)):
    # print("=" * 50)
    N = random.randint(1, n_range)
    K = random.randint(-1 * k_range, k_range)
    arr = [random.randint(-1 * arr_range, arr_range) for _ in range(N)]
    m, a = my(N, K, arr), answer(N, K, arr)
    if m != a:
        print("+" * 100)
        print(N, K, arr)
        print(m, a)
        print("+" * 100)
    # print("=" * 50)
