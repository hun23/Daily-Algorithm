from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")

def recur(idx, total):
    global N, ans
    if idx == N:
        if ans > total:
            ans = total
        return

    for n in range(N):
        if visited[n]:
            continue
        
        visited[n] = True
        for sale in sales[n]:
            potions[sale[0]] -= sale[1]
        
        to_add = potions[n] if potions[n] > 0 else 1
        recur(idx + 1, total + to_add)
        
        for sale in sales[n]:
            potions[sale[0]] += sale[1]
        
        visited[n] = False

N = int(input())
potions = list(map(int, input().split()))
sales = [list() for _ in range(N)]
for n in range(N):
    P = int(input())
    for p in range(P):
        a, d = map(int, input().split())
        sales[n].append((a - 1, d))

ans = 2147483647
visited = [False] * N
recur(0, 0)
println(ans)
