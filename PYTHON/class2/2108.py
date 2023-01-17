import sys

# import time

# f = open("./TESTCASE/2108.txt")
# n = int(f.readline())
n = int(sys.stdin.readline())
li = []
di = dict()
sum = 0
# start = time.time()
for _ in range(n):
    # num = int(f.readline())
    num = int(sys.stdin.readline())
    li.append(num)
    sum += num
    try:
        di[num] += 1
    except:
        di[num] = 1
li.sort()
# end = time.time()
# print(f"lisort{start - end}")

# start = time.time()
keys = []
mx = -2147483648
for key in di.keys():
    if di[key] > mx:
        mx = di[key]
        keys.clear()
        keys.append(key)
    elif di[key] == mx:
        keys.append(key)
keys.sort()
# end = time.time()
# print(f"keysort{start - end}")

print(round(sum / n))
print(li[round((n - 1) / 2)])
if len(keys) != 1:
    print(keys[1])
else:
    print(keys[0])
print(li[-1] - li[0])
