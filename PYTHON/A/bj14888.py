def recursion(arr, ops, answers, depth, cal):
    if depth == len(arr) - 1:
        answers.append(cal)
        return
    for i in range(4):
        if ops[i] == 0:
            continue
        op = "+-*/"[i]
        ops[i] -= 1
        temp = 0
        if op == "+":
            temp = cal + arr[depth + 1]
        elif op == "-":
            temp = cal - arr[depth + 1]
        elif op == "*":
            temp = cal * arr[depth + 1]
        elif op == "/":
            if cal < 0:
                temp = (abs(cal) // arr[depth + 1]) * -1
            else:
                temp = cal // arr[depth + 1]
        recursion(arr, ops, answers, depth + 1, temp)
        ops[i] += 1
    return

N = int(input())  # 2 <= <= 11
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))

# make operator list with recursion
# caculate
# compare minmax

answers = []
recursion(arr, ops, answers, 0, arr[0])
print(max(answers))
print(min(answers))