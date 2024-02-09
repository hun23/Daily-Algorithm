from sys import stdin, stdout

input = stdin.readline

def println(s):
    stdout.write(f"{s}\n")


def recur(idx, before, cnt, score):
    global ans
    if score + (10 - idx) < 5:
        return
    if idx == 10:
        ans += 1
        return
    
    for i in range(1, 6):
        selected[idx] = i
        if before == i:
            if cnt < 1:
                recur(idx + 1, before, cnt + 1, 
                    score + (1 if i == answers[idx] else 0))
        else:
            recur(idx + 1, i, 0, 
                score + (1 if i == answers[idx] else 0))


answers = list(map(int, input().split()))
selected = [0] * 10
ans = 0
recur(0, 0, 0, 0)
print(ans)
