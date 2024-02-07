from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")

def recur(idx, vowel_cnt, consonant_cnt):
    global L, C
    if idx == C:
        return
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        pass
    recur(idx + 1, )
    pass


L, C = map(int, input().split())
chars = list(input().split())
