from collections import deque

n = int(input())
arr = deque([i for i in range(1, n + 1)])
i = 0
while (len(arr) != 1):
    if (i % 2 == 0):
        arr.popleft()
    else:
        arr.append(arr.popleft())
    i = 1 if i == 0 else 0
print(arr[0])
