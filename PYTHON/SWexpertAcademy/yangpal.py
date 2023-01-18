import sys
from itertools import combinations
from itertools import permutations
import time
from tqdm import tqdm

global count
global n
global weights_sum
global fact
global weights

def recursion(visited, com, current_weight, idx):
    global count
    global n
    if idx == n:
        count += 1
        return
    if current_weight - sum(com) > 0:
        # count += fact[n - 1 - idx] * (2 ** (n - (idx + 1)))
        count += fact[n - idx] 
        return
    for (i, w) in enumerate(weights):
        if not visited[i]:
            visited[i] = True
            if w in com:
                current_weight -= w
                if current_weight >= 0:
                    recursion(visited, com[1:], current_weight, idx + 1)
            else:
                current_weight += w
                recursion(visited, com, current_weight, idx + 1)
            visited[i] = False
    return


f = open("C:\\Users\\SSAFY\\Desktop\\ssafy\\Daily-Algorithm\\Python\\SWexpertAcademy\\input.txt", 'r')
# t = int(sys.stdin.readline().rstrip())
t = int(f.readline().rstrip())
fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

for _ in range(t):
    count = 0
    # n = int(sys.stdin.readline().rstrip())
    n = int(f.readline().rstrip())
    start = time.time()
    # weights = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    weights = list(map(int, f.readline().rstrip().split(" ")))
    weights_sum = sum(weights)
    # global li
    # li = []
    for on_right_num in tqdm(range(0, n + 1)):
        for com in combinations(weights, on_right_num):
            com = list(com)
            if weights_sum / 2 >= sum(com):
                # 여기서부터 순서 고려
                # print(f"n:{on_right_num}, com:{com}")



                # Recursion & using factorial * 2**n
                visited = [False for _ in range(n)]
                recursion(visited, com, 0, 0)

                # BruteForce!
                # for per in permutations(weights, len(weights)):
                #     changing_sum = 0
                #     right_sum_left = sum(com)
                #     for w in per:
                #         if w in com:
                #             changing_sum -= w
                #         else:
                #             changing_sum += w
                #         if changing_sum < 0:
                #             break
                #     else:
                #         count += 1
    print(count)
    print(f"time: {time.time() - start:.5f} sec")
    f.close()
