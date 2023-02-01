def is_danjo(n):
    temp = n % 10
    n = n // 10
    while n != 0:
        rem = n % 10
        if rem > temp:
            return False
        n = n // 10
        temp = rem
    return True

T = int(input())
# danjo = dict()
for tc in range(1, T + 1):
    N = int(input())
    inp = list(map(int, input().split()))
    mx = -1
    # N = 1?
    if N == 1:
        if is_danjo(inp[0]):
            mx = inp[0]
    # ai * aj 계산
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            mult = inp[i] * inp[j]
            if mult > mx and is_danjo(mult):
                mx = mult
            # 겹치는 수가 많으면 효과가 있겠지만,
            # 아니었기 때문에 오히려 느려진 것 같다.
            # if danjo.get(mult) is None:
            #     danjo[mult] = is_danjo(mult)
            # if danjo[mult] and mult > mx:
            #     mx = mult
    print(f"#{tc} {mx}")
