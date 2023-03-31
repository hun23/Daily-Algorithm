import heapq
import sys

N = int(sys.stdin.readline().strip())
arr = []
for n in range(N):
    num = int(sys.stdin.readline().strip()) * -1
    if num != 0:
        heapq.heappush(arr, num)
    else:
        if len(arr) != 0:
            print(heapq.heappop(arr) * -1)
        else:
            print(0)
