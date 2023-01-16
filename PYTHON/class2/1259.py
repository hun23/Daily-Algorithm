import sys

while True:
    inp = str(sys.stdin.readline().rstrip())
    p = True
    if inp == "0":
        break
    _len = len(inp)
    for i in range(_len//2):
        if inp[i] != inp[_len - 1 - i]:
            p = False
            break
    if p:
        print("yes")
    else:
        print("no")