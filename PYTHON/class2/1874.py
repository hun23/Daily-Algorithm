import sys


def push(ascend, temp, output):
    output.append("+")
    temp.append(ascend[0])
    del ascend[0]


def pop(temp, arr, output):
    output.append("-")
    arr.append(temp[-1])
    del temp[-1]


n = int(input())
inp = []
ascend = list(range(1, n + 1))
arr = []
temp = []
for _ in range(n):
    inp.append(int(sys.stdin.readline().rstrip()))

filled = 0
output = []
no = 0
while True:
    if len(temp) != 0 and temp[-1] == inp[filled]:
        pop(temp, arr, output)
        filled += 1
    else:
        try:
            push(ascend, temp, output)
        except:
            no = 1
            break
    if arr == inp:
        break
if no:
    print("NO")
else:
    for i in output:
        print(i)
