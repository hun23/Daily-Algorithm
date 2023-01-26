import sys

while True:
    inp = sys.stdin.readline().rstrip()
    if inp == ".":
        break
    stack = []
    for c in inp:
        if c == "(":
            stack.append(c)
        elif c == "[":
            stack.append(c)
        elif c == ")":
            try:
                if stack.pop() != "(":
                    print("no")
                    break
            except:
                print("no")
                break
        elif c == "]":
            try:
                if stack.pop() != "[":
                    print("no")
                    break
            except:
                print("no")
                break
        if c == ".":
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
            break
