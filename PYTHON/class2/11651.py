import sys

n = int(input())
di = dict()
for _ in range(n):
    # y = k 라면 di[k]에 있는 리스트에 num을 추가한다
    num = tuple(map(int, sys.stdin.readline().rstrip().split(" ")))
    if di.get(num[1]) == None:  # y=k인 원소가 처음 들어가면
        li = [num]
        di[num[1]] = li  # (~, k)를 가진 리스트를 넣는다.
    else:
        di[num[1]].append(num)
# di를 key순으로 정렬한 리스트를 순회하며
for key in sorted(di.items(), key=lambda x: x[0]):
    # di[key]를 x로 정렬하여 다시 순회한다
    li = sorted(key[1], key=lambda x: x[0])
    for num in li:
        print(str(num[0]) + " " + str(num[1]))
