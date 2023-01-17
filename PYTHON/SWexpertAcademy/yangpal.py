import sys
from itertools import combinations
from itertools import permutations
import time
from tqdm import tqdm

# def recursion(visited, weights, com, n, current_weight, idx):
#     global count
#     if idx == n:
#         count += 1
#         return
#     for (i, w) in enumerate(weights):
#         if not visited[i]:
#             if w in com:
#                 current_weight -= w
#             else:
#                 current_weight += w
#             if current_weight < 0:
#                 pass
#             else:
#                 visited[i] = True
#                 recursion(visited, weights, com, n, current_weight, idx + 1)
#                 visited[i] = False
#     return


f = open("C:\\Users\\SSAFY\\Desktop\\ssafy\\Daily-Algorithm\\Python\\SWexpertAcademy\\input.txt", 'r')
# t = int(sys.stdin.readline().rstrip())
t = int(f.readline().rstrip())
for _ in range(t):
    # n = int(sys.stdin.readline().rstrip())
    n = int(f.readline().rstrip())
    start = time.time()
    # weights = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    weights = list(map(int, f.readline().rstrip().split(" ")))
    weights_sum = sum(weights)
    # global count
    # global li
    # li = []
    count = 0
    for on_right_num in tqdm(range(0, n + 1)):
        for com in combinations(weights, on_right_num):
            if weights_sum / 2 >= sum(com):
                # 여기서부터 순서 고려
                # print(f"n:{on_right_num}, com:{com}")
                # visited = [False for _ in range(n)]
                # recursion(visited, weights, com, n, 0, 0)
                di = dict()
                for per in permutations(weights, len(weights)):
                    changing_sum = 0
                    right_sum_left = sum(com)
                    li = []
                    for w in per:
                        if w in com:
                            li.append(-1 * w)
                        else:
                            li.append(w)
                        if di.get(tuple(li)):
                            changing_sum = di[tuple(li)]
                        else:
                            if w in com:
                                changing_sum -= w
                            else:
                                changing_sum += w
                            di[tuple(li)] = changing_sum
                        if changing_sum < 0:
                            break
                    else:
                        count += 1
print(count)
print(f"time: {time.time() - start:.5f} sec")
f.close()
