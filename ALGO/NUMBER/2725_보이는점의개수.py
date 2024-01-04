from sys import stdin, stdout
input = stdin.readline
print = stdout.write

C = int(input())
for c in range(C):
    N = int(input())

# 6 - 1 2(1/3) 3(1/2) 4(2/3) 5 6(1/1)
# 5 - 1 2 3 4 5(1/1)
# 4 - 1 2(1/2) 3 4(1/1)
# 3 - 1 2 3(1/1)
# 2 - 1 2(1/1)
# 1 - 1