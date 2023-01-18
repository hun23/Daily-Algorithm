import sys

def is_jikgak(a, b, c):
    # 제일 긴 변
    mx = max(a, b, c)
    li = [a, b, c]
    # a**2 + b**2 저장위한 변수
    ab = 0
    for _len in li:
        # 제일 긴 변을 제외한 값을 제곱해서 더한다
        if _len != mx:
            ab += _len ** 2
    # a**2 + b**2 == c**2
    if ab == mx ** 2:
        return True
    return False

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == b == c == 0:
        break
    if is_jikgak(a, b, c):
        print("right")
    else:
        print("wrong")
    