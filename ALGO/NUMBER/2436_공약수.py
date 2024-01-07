from sys import stdin, stdout
input = stdin.readline
inputs = input().split
print = stdout.write

def println(s):
    print(f"{s}\n")

def divide(num):
    ret = dict()
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            ret[i] = ret.get(i, 0) + 1
            num //= i
    if num != 1:
        ret[num] = 1
    return ret

G, L = map(int, inputs())
L_divided = divide(L)
G_divided = divide(G)
# 각 값에 G를 넣고
# L을 G로 나눈 만큼을 각 값에 분배해서 합이 최소가 되게
# 어떻게?
# brute-force
# 경우의수 2의 최대인수개수를 제곱한 만큼
# == 결국 n만큼 경우의 수, 10억이니까 될지도?
ans, wer = 1, 1
