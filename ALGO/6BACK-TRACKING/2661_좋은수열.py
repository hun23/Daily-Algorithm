from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def is_good(idx):
    global N, selected
    diff = 1
    while 0 <= idx - diff:
        left, right = idx - diff, idx
        bad = True
        cnt = 0
        while cnt < diff:
            if selected[left] != selected[right]:
                bad = False
                break
            left -= 1
            right -= 1
            cnt += 1
        if bad:
            return False
        diff += 1
    return True


def recur(idx):
    global N, selected
    if idx == N:
        print("".join(map(str, selected)))
        exit()
    for i in range(1, 4):
        selected[idx] = i
        if is_good(idx):
            recur(idx + 1)


N = int(input())
selected = [0] * N
recur(0)
