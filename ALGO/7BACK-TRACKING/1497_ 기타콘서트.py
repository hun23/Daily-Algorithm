from sys import stdin, stdout

input = stdin.readline


def println(s):
    print(f"{s}\n")

def to_bit(songs):
    global M
    ret = 0
    for i in range(M):
        if songs[i] == "Y":
            ret = ret | (1 << (M - i - 1))
    return ret

def bit_count(bit):
    ret = 0
    while bit > 0:
        if bit % 2 == 1:
            ret += 1
        bit = bit >> 1
    return ret

def recur(idx, cnt, bits):
    global N, M, ans, guitars
    if idx == N:
        bc = bit_count(bits)
        if bc > ans[1]:
            ans[0] = cnt
            ans[1] = bc
            return cnt
        elif bc == ans[1] and cnt < ans[0]:
            ans[0] = cnt
            return
        return

    recur(idx + 1, cnt, bits),
    recur(idx + 1, cnt + 1, bits | guitars[idx])
    return

N, M = map(int, input().split())
guitars = []
for n in range(N):
    _, songs = input().split()
    guitars.append(to_bit(songs))
ans = [2147483647, 0]
recur(0, 0, 0)
ans = ans[0] if ans[1] != 0 else -1
print(ans)
