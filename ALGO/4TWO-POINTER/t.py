import random

with open("./memo.txt", "w") as fr:
    T = 10
    fr.write(f"{T}\n")
    for t in range(T):
        k = random.randint(1, 40_000_000)
        N = 1000
        fr.write(f"{k} {N}\n")
        for i in range(4):
            for n in range(N):
                fr.write(f"{random.randint(1, 10_000_000)}")
                if n != N - 1:
                    fr.write(" ")
                else:
                    fr.write("\n")
