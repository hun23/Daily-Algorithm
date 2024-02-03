from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")

def possible(idx, n):
    global selected, numbers
    # is it possible to put 'n' on 'idx'th selected number?
    

def recur(idx, start):
    global N, selected, numbers
    if idx == 3:
        print(selected)
        return
    for n in range(start, 1_000_000_000):
        if possible(idx, n):
            selected[idx] = n
            recur(idx + 1, n)

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = 0
    selected = [0] * 3
    recur(0, 1)
    
#   A   B   C   A+B A+C B+C ABC
    2   2   5   4   7   7   11
    