from sys import stdin, stdout

input = stdin.readline


def println(s):
    stdout.write(f"{s}\n")


def recur(idx, start, vowel_cnt, consonant_cnt):
    global L, C, chars, selected
    if idx == L:
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print("".join(selected))
        return
    for i in range(start, C):
        selected[idx] = chars[i]
        vc, cc = (1, 0) if chars[i] in "aeiou" else (0, 1)
        recur(idx + 1, i + 1, vowel_cnt + vc, consonant_cnt + cc)


L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
selected = ["0"] * L
recur(0, 0, 0, 0)
