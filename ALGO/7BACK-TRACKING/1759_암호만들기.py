from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")

def recur(idx, vowel_cnt, consonant_cnt, selected):
    global L, C
    if vowel_cnt + consonant_cnt == L and vowel_cnt >= 1 and consonant_cnt >= 2:
        print(selected)
        return
    
    if idx == C:
        return

    if chars[idx] in "aeiou":
        recur(idx + 1, vowel_cnt + 1, consonant_cnt, selected + chars[idx])
    else:
        recur(idx + 1, vowel_cnt, consonant_cnt + 1, selected + chars[idx])
    recur(idx + 1, vowel_cnt, consonant_cnt, selected)
    return


L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
recur(0, 0, 0, "")
