N = int(input())
li = []
for _ in range(N):
    n = int(input())
    li.append(n)
    li.sort()
for i in li:
    print(i)