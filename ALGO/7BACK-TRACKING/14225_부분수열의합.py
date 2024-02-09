from sys import stdin, stdout


input = stdin.readline


def println(s):
    print(f"{s}\n")

def recur(idx, total):
    global N
    if idx == N:
        results.append(total)
        return
    recur(idx + 1, total + arr[idx])
    recur(idx + 1, total)
    return

N = int(input())
arr = list(map(int, input().split()))
results = []
recur(0, 0)
results.sort()

ans = 0
for i in range(1, 1 << N):
    if results[i] - results[i - 1] > 1:
        print(results[i - 1] + 1)
        exit()
print(results[-1] + 1)

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip())
S = list(map(int, input().split()))



def sol():
    S.sort()
    
    if S[0] > 1:
        print(1)
        return
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        if S[i] > dp[i - 1] + 1:
            print(dp[i - 1] + 1)
            return
        else:
            dp[i] = dp[i - 1] + S[i]
    print(dp[N - 1] + 1)


sol()
???????

"""