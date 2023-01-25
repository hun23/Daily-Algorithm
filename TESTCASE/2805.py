import random

n = 1000000
m = 2000000000
h = 1000000000
f = open("./TESTCASE/2805.txt", "w")
f.write(f"{n} {m}\n")
li = []
while sum(li) < m:
    li.clear()
    for _ in range(n):
        num = random.randint(0, h)
        li.append(num)
        f.write(str(num) + " ")
f.close()
