import sys
# 별, 동그라미, 네모, 세모
# 4, 3, 2, 1

# 입력줄을 받아 각 도형(1 ~ 4)의 개수를 센 딕셔너리를 반환
def counting_star(inp):
    ret = {i:0 for i in range(1, 5)}
    for i in inp[1:]:
        ret[i] += 1
    return ret


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    inp = list(map(int, sys.stdin.readline().rstrip().split()))
    a = counting_star(inp)  # a 도형 개수 입력
    inp = list(map(int, sys.stdin.readline().rstrip().split()))
    b = counting_star(inp)  # b 도형 개수 입력
    for i in range(4, 0, -1):  # 별(4)부터 순서대로 개수 비교
        if a[i] > b[i]:
            print("A")
            break
        elif a[i] < b[i]:
            print("B")
            break
    else:
        print("D")  # 모든 도형에서 개수가 같은 경우
