from collections import deque

# recursion error
# def dp(d, n):
#     if n <= 1:
#         return d[n]
#     if d.get(n) != None:
#         return d[n]
#     path = [
#         dp(d, n // 3 if n % 3 == 0 else 0) + 1,
#         dp(d, n // 2 if n % 2 == 0 else 0) + 1,
#         dp(d, n - 1) + 1,
#     ]
#     d[n] = min(path)
#     return d[n]


n = int(input())
count = 0
d = dict()
d[0] = 2147483647
d[1] = 0
# print(dp(d, n))

# BFS
q = deque()
q.append(n)
count = dict()
count[n] = 0
while q:
    node = q.popleft()
    if count.get(1) != None:
        break
    c = count[node]
    if node % 3 == 0:
        q.append(node // 3)
        if count.get(node // 3) == None:
            count[node // 3] = c + 1
        else:
            count[node // 3] = min(c + 1, count[node // 3] + 1)
    if node % 2 == 0:
        q.append(node // 2)
        if count.get(node // 2) == None:
            count[node // 2] = c + 1
        else:
            count[node // 2] = min(c + 1, count[node // 2] + 1)
    q.append(node - 1)
    if count.get(node - 1) == None:
        count[node - 1] = c + 1
    else:
        count[node - 1] = min(c + 1, count[node - 1] + 1)

print(count[1])
# dp
# for i in range(1, n + 1):
#     if d.get(i) != None:
#         continue
#     path = [
#         d[i // 3 if i % 3 == 0 else 0] + 1,
#         d[i // 2 if i % 2 == 0 else 0] + 1,
#         d[i - 1] + 1,
#     ]
#     d[i] = min(path)
# print(d[n])
