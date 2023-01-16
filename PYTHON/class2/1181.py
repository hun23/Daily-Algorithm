import sys

n = int(input())
arr = []
lens = [list() for _ in range(50)]
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    arr.append(word)
    lens[len(list(word)) - 1].append(word)
for li in lens:
    li.sort()
    temp = ""
    for l in li:
        if temp != l:
            print(l)
        temp = l
