import sys

# 메모리 초과
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().rstrip()))
# arr.sort()
# for num in arr:
#     print(num)


n = int(input())
arr = []
# 숫자가 나타난 횟수를 저장할 dictionary
di = dict()
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if di.get(num) == None:  # 처음 등장한 숫자면
        di[num] = 1  # 횟수 = 1
        arr.append(num)  # 정렬 위해 arr에 추가
    else:
        di[num] += 1  # 다시 등장하면 횟수 +1
# 정렬
arr.sort()
for num in arr:
    # dictionary에 저장한 횟수만큼 출력
    for value in range(di[num]):
        print(num)
