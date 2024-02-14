from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


N = int(input())
members = [list(map(int, input().split())) + [n] for n in range(N)]
used = [False] * N
ans = 0
sorted_members = {
    "a": sorted(members, key=lambda x:x[0], reverse=True),
    "b": sorted(members, key=lambda x:x[1], reverse=True),
    "c": sorted(members, key=lambda x:x[2], reverse=True),
    "d": sorted(members, key=lambda x:x[3], reverse=True),
    "e": sorted(members, key=lambda x:x[4], reverse=True),
}
for a in sorted_members["a"][:5]:
    for b in sorted_members["b"][:5]:
        if a[5] == b[5]:
            continue
        for c in sorted_members["c"][:5]:
            if a[5] == c[5] or b[5] == c[5]:
                continue
            for d in sorted_members["d"][:5]:
                if a[5] == d[5] or b[5] == d[5] or c[5] == d[5]:
                    continue
                for e in sorted_members["e"][:5]:
                    if a[5] == e[5] or b[5] == e[5] or c[5] == e[5] or d[5] == e[5]:
                        continue
                    temp = a[0] + b[1] + c[2] + d[3] + e[4]
                    if temp > ans:
                        ans = temp
println(ans)
exit()


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
