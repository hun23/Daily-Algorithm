from sys import stdin, stdout
import random
from tqdm import tqdm
input = stdin.readline



def score(a, b, c):
    return abs(max(a, b, c) - min(a, b, c))

def forloop(A, B, C, A_list, B_list, C_list):
    ans = 2 * 100_000_000 + 1
    for a in range(A):
        for b in range(B):
            for c in range(C):
                temp = score(A_list[a], B_list[b], C_list[c])
                if ans > temp:
                    ans = temp
    return ans

def binary(A, B, C, A_list, B_list, C_list):
    ans = 2 * 100_000_000 + 1
    for a in A_list:
        for b in B_list:
            big, small = (a, b) if a > b else (b, a)
            if big - small >= ans:
                continue

            left, right = 0, C - 1
            while left <= right:
                mid = (left + right) // 2
                if big >= C_list[mid] >= small:
                    ans = min(ans, big - small)
                    break
                if C_list[mid] < small:
                    left = mid + 1
                elif C_list[mid] > big:
                    right = mid - 1
            
            if C > left >= 0:
                ans = min(ans, score(big, small, C_list[left]))
            if 0 <= right < C:
                ans = min(ans, score(big, small, C_list[right]))
    return ans

T = 10000
len_limit = 100
limit = 100
for t in tqdm(range(T)):
    A, B, C = random.randint(1, len_limit), random.randint(1, len_limit), random.randint(1, len_limit)
    A_list = sorted([random.randint(-limit, limit) for i in range(A)])
    B_list = sorted([random.randint(-limit, limit) for i in range(B)])
    C_list = sorted([random.randint(-limit, limit) for i in range(C)])
    zzz, xxx = forloop(A, B, C, A_list, B_list, C_list), binary(A, B, C, A_list, B_list, C_list)
    if zzz != xxx:
        print(f"{A} {B} {C}")
        print(*A_list)
        print(*B_list)
        print(*C_list)
        print(f"{zzz} {xxx}")
        print("=" * 100)