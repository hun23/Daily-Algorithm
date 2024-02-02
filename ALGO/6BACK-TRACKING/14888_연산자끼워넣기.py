from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, val):
    global N, func, numbers, ans
    if idx == N - 1:
        if val > ans[0]:
            ans[0] = val
        if val < ans[1]:
            ans[1] = val
        return
    for op in range(4):
        if operators[op] == 0:
            continue
        operators[op] -= 1
        recur(idx + 1, func[op](val, numbers[idx + 1]))
        operators[op] += 1


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if a < 0:
        return (abs(a) // b) * -1
    return a // b


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
func = [plus, minus, mult, div]
ans = [-2147483648, 2147483647]
recur(0, numbers[0])
print(*ans, sep="\n")
