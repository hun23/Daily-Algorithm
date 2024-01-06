from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())
numbers = list(map(int, input().split()))

total = dict()
divided_list = []
for num in numbers:
    # 소인수분해
    temp = dict()
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            total[i] = total.get(i, 0) + 1
            temp[i] = temp.get(i, 0) + 1
            num //= i
    if num != 1:
        temp[num] = 1
    # print(f"temp: {temp}\n")
    divided_list.append(temp)
    
# target 만들기 - 다 곱하고 각 소인수를 N개로 나눈 만큼 가지도록
target = dict()
for key, val in total.items():
    target[key] = val // N

# 횟수 구하기
ans = 0
target_val = 1
for key, val in target.items():
    target_val *= (key**val)
    # print(f"key:{key}, val: {val}\n")
    for divided in divided_list:
        ans += abs(val - divided.get(key, 0))
        # print(f"ans:{ans}\n")
print(f"{target_val} {ans//2}\n")
