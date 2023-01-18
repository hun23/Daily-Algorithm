import random

n = 500000
m = 500000
li = []
f = open("./TESTCASE/test.txt", "w")
f.write(str(n) + "\n")
for _ in range(n):
    num = random.randint(-10000000, 10000000)
    li.append(num)
    f.write(str(num) + " ")
f.write("\n" + str(m) + "\n")
li = []
for _ in range(m):
    num = random.randint(-10000000, 10000000)
    li.append(num)
    f.write(str(num) + " ")
f.close()