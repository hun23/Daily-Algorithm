li = []
for _ in range(5):
    n = int(input())
    li.append(n)
print(round(sum(li)/5))
li.sort()
print(li[2])