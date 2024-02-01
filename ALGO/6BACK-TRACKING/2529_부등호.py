from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx):
    global K, arr, numbers, visited, check
    if idx == K + 1:
        ans.append("".join(list(map(str, numbers))))
        return
    for n in range(10):
        if visited[n]:
            continue
        if not check[arr[idx - 1]](numbers[idx - 1], n):
            continue
        visited[n] = True
        numbers[idx] = n
        recur(idx + 1)
        visited[n] = False

def less_than(a, b):
    return a < b

def greater_than(a, b):
    return a > b

check = {
    "<": less_than,
    ">": greater_than
}

K = int(input())
arr = list(input().split())
numbers = [0] * (K + 1)
visited = [False] * 10
ans = []
for start in range(10):
    numbers[0] = start
    visited[start] = True
    recur(1)
    visited[start] = False
ans.sort(reverse=True)
print(ans[0])
print(ans[-1])
