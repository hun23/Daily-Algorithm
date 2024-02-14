import random
from tqdm import tqdm
from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")

def recur(idx, total, last_val):
    global N
    if idx == N:
        return total + last_val
    elif idx > N:
        return total
    else:
        total += last_val

    return max(
        recur(idx + arr[idx][0], total, arr[idx][1]),
        recur(idx + 1, total, 0)
    )

def recurDP(idx, total, last_val):
    global N
    # if idx == 0:
    #     return total + last_val
    if idx < 0:
        return total
    else:
        total += last_val

    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(
        recurDP(idx - arr[idx][0], total, arr[idx][1]), recurDP(idx - 1, total, 0)
    )
    return dp[idx]


# N = int(input())
# arr = [tuple(map(int, input().split())) for _ in range(N)]
# dp = [-1] * N
# println(recur(0, 0, 0))
# println(recurDP(0, 0, 0))

# for N in range(1, 16):
#     for T in range(1, 6):
#         for P in range(1, 1001):
            

T = 10000000
for t in tqdm(range(T)):
    N = random.randint(1, 15)
    arr = []
    for n in range(N):
        arr.append((random.randint(1, 5), random.randint(1, 1000)))
    dp = [-1] * N
    a = recur(0, 0, 0)
    b = recurDP(N - 1, 0, 0)
    if a != b:
        print("=" * 50)
        print(a, b)
        print(N, arr)
        exit()




