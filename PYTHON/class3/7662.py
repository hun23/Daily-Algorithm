import sys
import heapq

T = int(sys.stdin.readline().strip())
for tc in range(1, T + 1):
    K = int(sys.stdin.readline().strip())
    min_heap, max_heap = [], []
    dead = []

    for k in range(K):
        op, num = sys.stdin.readline().strip().split()
        num = int(num)
        print(f"min: {min_heap} / max: {max_heap} / dead: {dead}")
        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, num * -1)
            continue
        if len(min_heap) != 0:
            if num == -1:   # delete min value
                while len(dead) and len(min_heap) and min_heap[0] in dead:
                    dead.remove(min_heap[0])
                    heapq.heappop(min_heap)
                if len(min_heap):
                    popped = heapq.heappop(min_heap)
                    dead.append(popped)
            else:           # delete max value
                while len(dead) and len(max_heap) and max_heap[0] in dead:
                    dead.remove(max_heap[0] * -1)
                    heapq.heappop(max_heap)
                if len(max_heap):
                    popped = heapq.heappop(max_heap)
                    dead.append(popped * -1)

    if len(min_heap) != 0:
        print(max_heap[0] * -1, min_heap[0])
    else:
        print("EMPTY")

