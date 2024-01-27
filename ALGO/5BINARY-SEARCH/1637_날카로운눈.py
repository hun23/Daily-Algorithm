from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def how_many(numbers, num):
    global N
    # num이 A보다 크거나 같은 최소 idx 찾기
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid][0] <= num:
            left = mid + 1
        else:
            right = mid - 1
    A_start = right

    # 같은 A를 가진 numbers 내에서 C가 num코다 크거나 같은 최소 idx 찾기
    left, right = A_start, ?
    
    println(f"num:{num} idx:{right}")
    return 0


N = int(input())
numbers = []
start, end = 2147483647, 0
for n in range(N):
    a, b, c = tuple(map(int, input().split()))
    if a < start:
        start = a
    if end < b:
        end = b
    numbers.append((a, b, c))
numbers.sort(key=lambda x: (x[1], x[0], x[2]))

"""
1. 어떤 수가 홀수개인지 어떻게 알 수 있나
C가 해당 수 보다 작은 경계를 이분탐색으로 찾아서
그 안에서 (N - A)%B==0인지 확인한다
    a. A를 기준으로 이분탐색해서 N이 등장 가능한지 확인
    b. C를 기준으로 이분탐색해서 N이 등장 가능한지 확인
    c. A를 기준으로 하고, C를 기준으로는 굳이 어차피 순회할건데?
    d. A기준으로 자르고, 같은 A를 가진 idx 내에서는 C로 정렬되어 있으니 또분탐색
2. 어떤 수를 어떻게 정하나
    a. start ~ end 돌기
    b. ???
3. 
"""
for num in range(start, end + 1):
    cnt = how_many(numbers, num)
    println(f"num: {num}, cnt: {cnt}")
    # if cnt % 2 == 1:
    #     println(f"{num} {cnt}")
    #     exit()
println("NOTHING")
