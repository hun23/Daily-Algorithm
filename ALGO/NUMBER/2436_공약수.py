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

def get_GCD(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b

def make_answer(numbers, ans, wer, idx):
    global G
    if get_GCD(ans, wer) > G:
        return (2147483647, 2147483647)
    if idx >= len(numbers):
        return (ans, wer) if ans < wer else (wer, ans)
    case1 = make_answer(numbers, ans * numbers[idx], wer, idx + 1)
    case2 = make_answer(numbers, ans, wer * numbers[idx], idx + 1)
    if case1[0] + case1[1] > case2[0] + case2[1]:
        return case2
    return case1
    
    
G, L = map(int, inputs())
L_divided = divide(L)
G_divided = divide(G)
numbers = []
for key, val in L_divided.items():
    while val > 0:
        numbers.append(key)
        val -= 1
for key, val in G_divided.items():
    while val > 0:
        numbers.remove(key)
        val -= 1
# println(numbers)
# 각 값에 G를 넣고
# L을 G로 나눈 만큼을 각 값에 분배해서 합이 최소가 되게
# 어떻게?
# brute-force
# 경우의수 2의 최대인수개수를 제곱한 만큼
# == 결국 n만큼 경우의 수, 10억이니까 될지도?

ans, wer = make_answer(numbers, G, G, 0)
print(f"{ans} {wer}")

# 2 / 2 2 2 2 2 2 3 3 3 5 5 7 11 13

# 2 2 2 2 2 3 3 3 5 5 7 11 13
# 13104 / 13200
# 2 2 2 2 3 3 7 13 / 2 2 2 2 3 5 5 11
# 2 - 8개 ?
# 3 - 3개
# 5 - 2개
# 7, 11, 13 각 1개
# 이러면 최대공약수가 2보다 커지는구나!

# [2, 2, 2, 2, 2, 2, 2, 7, 13]
# [2, 3, 3, 3, 5, 5, 11]
# 2 2 2 2 2 2 2 2 - 8개
# 3 3 3, 5 5, 7, 11, 13