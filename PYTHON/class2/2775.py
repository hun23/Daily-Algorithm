import sys


def how_many(apart, k, n):
    # 값이 이미 있는 경우
    if apart[k][n] != 0:
        return apart[k][n]
    sum = 0
    # 아래층(k - 1)에서 1호(=인덱스는 1-1=0)
    # ~ n호(마찬가지로 인덱스는 n-1까지 순회
    for i in range(n + 1):
        sum += how_many(apart, k - 1, i)
    # 얻은 값 저장
    apart[k][n] = sum
    return sum


# 입력
t = int(input())
# 0~14층, 1~14호 [15][14]배열 만들기
# 0층에는 값(col + 1) 입력
apart = [
    [0 if row != 0 else col + 1 for col in range(14)]
    for row in range(15)
]
answer = []
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    # 재귀함수 시작
    answer.append(how_many(apart, k, n - 1))
for a in answer:
    print(a)
