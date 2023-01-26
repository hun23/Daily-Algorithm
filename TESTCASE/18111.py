import random

n = 500
m = 500
b = random.randint(0, 6.4 * 10**7)
f = open("./TESTCASE/18111.txt", "w")
f.write(" ".join(map(str, [n, m, b])) + "\n")
for _ in range(n):
    m_arr = [str(random.randint(0, 256)) for _ in range(m)]
    f.write(" ".join(m_arr) + "\n")
f.close()
