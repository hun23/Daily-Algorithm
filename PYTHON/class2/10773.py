import sys

n = int(input())
li = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        li.pop()
    else:
        li.append(num)
print(sum(li))
