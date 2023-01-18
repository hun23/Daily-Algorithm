import sys

t = int(input())
for _ in range(t):
    arr = sys.stdin.readline().rstrip()
    # 괄호 개수 세기
    count  = 0
    for c in arr:
        if c == '(':
            count += 1
        else:
            count -= 1
        # count가 음수 => ")"가 더 많다
        if count < 0:
            print("NO")
            break
    else:
        if count == 0:
            print("YES")
        # count가 양수 => "("가 더 많다
        else:
            print("NO")
