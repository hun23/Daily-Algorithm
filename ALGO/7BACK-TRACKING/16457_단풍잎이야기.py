from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")

def cnt(selected):
    global skills_for_quest
    ret = 0
    for skills in skills_for_quest:
        good = True
        for skill in skills:
            if skill not in selected:
                good = False
        if good:
            ret += 1
    return ret

def recur(idx, selected):
    global N
    if  len(selected) == N or idx == 2 * N:
        return cnt(selected)
    
    return max(
        recur(idx + 1, selected + [idx + 1]),
        recur(idx + 1, selected)
    )

N, M, K = map(int, input().split())
skills_for_quest = [list(map(int, input().split())) for _ in range(M)]
print(recur(0, []))
