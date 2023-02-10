import sys

global S


def add(x):
    global S
    if not check(x):
        S += 2 ** (x - 1)
    return


def remove(x):
    global S
    if check(x):
        S -= 2 ** (x - 1)
    return


def check(x, prnt=False):
    global S
    if S & (1 << (x - 1)):
        if prnt:
            print(1)
        return True
    else:
        if prnt:
            print(0)
        return False


def toggle(x):
    global S
    if check(x):
        S -= 2 ** (x - 1)
    else:
        S += 2 ** (x - 1)


def all():
    global S
    S = 2**20 - 1
    return


def empty():
    global S
    S = 0
    return


def do_op(op, x):
    if op == "add":
        add(x)
    elif op == "remove":
        remove(x)
    elif op == "check":
        check(x, True)
    elif op == "toggle":
        toggle(x)


M = int(sys.stdin.readline().rstrip())
S = 0
for m in range(M):
    inp = sys.stdin.readline().rstrip().split()
    if len(inp) == 1:
        if inp[0] == "all":
            all()
        else:
            empty()
    else:
        do_op(inp[0], int(inp[1]))
