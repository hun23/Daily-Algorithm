from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


def how_many(num):
    global numbers, N
    # num이 A보다 큰 최소 idx 찾기
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid][0] > num:
            right = mid - 1
        else:
            left = mid + 1
    # left 밑으로 홀수개인지 알아보기
    # new_numbers = sorted(numbers[:left], key=lambda x: x[1])
    # left, right = 0, len(new_numbers) - 1
    # while left <= right:
    #     mid = (left + right) // 2
    #     if new_numbers[mid][1] < num:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    cnt = 0
    # for a, c, b in new_numbers[left:]:
    for a, c, b in numbers[:left]:
        if c < num:
            continue
        if (num - a) % b == 0:
            cnt += 1
    # println(f'num:{num}, left:{left}, cnt:{cnt}')
    return cnt


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
numbers.sort()
"""
1. 어떤 수가 홀수개인지 어떻게 알 수 있나
A가 해당 수 보다 큰 경계를 이분탐색으로 찾아서
그 밑에서 (N - A)%B==0인지 확인한다
2. 어떤 수를 어떻게 정하나
    a. start ~ end 돌기
    b. ???
1 2 3 4 5 6 7 8 9 10
      4
1 2 3 4 5
          6 7 8 9 10
"""
for num in range(start, end + 1):
    cnt = how_many(num)
    if cnt % 2 == 1:
        println(f"{num} {cnt}")
        exit()
println("NOTHING")
