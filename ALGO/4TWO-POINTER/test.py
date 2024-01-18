from sys import stdin, stdout
import time
from tqdm import tqdm

with open("./memo.txt", "r") as f:

    input = f.readline
    # input = stdin.readline
    print = stdout.write


    def println(s):
        print(f"{s}\n")


    T = int(input())
    for t in range(T):
        K, N = map(int, input().split())
        arr = [sorted(list(map(int, input().split()))) for _ in range(4)]

        ans = sum(arr[i][0] for i in range(4))

        pairs = [[], []]
        for a in range(N):
            for b in range(N):
                pairs[0].append(arr[0][a] + arr[1][b])
        for c in range(N):
            for d in range(N):
                pairs[1].append(arr[2][c] + arr[3][d])
        pairs[0].sort()
        pairs[1].sort()

        result = [0, 40_000_001]
        left, right = 0, len(pairs[1]) - 1
        while left < len(pairs[0]) and 0 <= right:
            temp_sum = pairs[0][left] + pairs[1][right]
            if temp_sum > K:
                right -= 1
                if temp_sum < result[1]:
                    result[1] = temp_sum
            elif temp_sum < K:
                left += 1
                if temp_sum > result[0]:
                    result[0] = temp_sum
            else:
                result[0], result[1] = temp_sum, temp_sum
                break
        for r in result:
            if r == 0 or r == 40_000_001:
                continue
            if abs(K - r) < abs(K - ans):
                ans = r
            elif abs(K - r) == abs(K - ans) and r < ans:
                ans = r
        println(f"{ans}")
