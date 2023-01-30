import time
from itertools import combinations
from collections import deque

f = open("./TESTCASE/yangpal.txt", "r")
# t = int(sys.stdin.readline().rstrip())
t = int(f.readline().rstrip())
fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

for _ in range(t):
    answer = 0
    # n = int(sys.stdin.readline().rstrip())
    n = int(f.readline().rstrip())
    start = time.time()
    # weights = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    weights = list(map(int, f.readline().rstrip().split(" ")))
    weights_sum = sum(weights)
    graph = dict()
    for i in range(0, n):
        graph[i] = list(filter(lambda x: x != i, range(n)))
    for on_left_num in range(0, n + 1):
        for lefts in combinations(weights, on_left_num):
            lefts = list(lefts)
            if sum(lefts) * 2 >= weights_sum:
                for le in lefts:
                    visited = [False] * n
                    q = deque()
                    q.append(le)
                    lsum = weights[le]
                    while q:
                        node = graph[q.pop()]
                        for next in node:
                            if not visited[next]:

                                q.append(next)

    print(answer)
    print(f"time: {time.time() - start:.5f} sec")
f.close()
