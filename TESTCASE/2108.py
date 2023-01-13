import random

n = 500000
li = []
f = open("./TESTCASE/2108.txt", "w")
f.write(str(n) + "\n")
for _ in range(n):
    num = random.randint(-4000, 4000)
    li.append(num)
    f.write(str(num) + "\n")
print(li[:100])
f.close()