import sys
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
t = int(input())
arr = []
# t개 수 입력
for _ in range(t):
    arr.append(int(sys.stdin.readline().rstrip()))
# 정렬
arr.sort()
for i in arr:
    print(i)
