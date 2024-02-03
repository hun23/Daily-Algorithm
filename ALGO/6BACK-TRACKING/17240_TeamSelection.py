from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


N = int(input())
members = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for a in range(N):
    for b in range(N):
        if a == b:
            continue
        for c in range(N):
            if a == c or b == c:
                continue
            for d in range(N):
                if a == d or b == d or c == d:
                    continue
                for e in range(N):
                    if a == e or b == e or c == e or d == e:
                        continue
                    temp = (
                        members[a][0]
                        + members[b][1]
                        + members[c][2]
                        + members[d][3]
                        + members[e][4]
                    )
                    if temp > ans:
                        ans = temp
println(ans)
