from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    inp = input()

    # make deque of nums
    q = deque()
    for i in inp:
        q.append(int(i, 16))

    # rotate
    possibles = set()
    for n in range(N//4):  # rotation
        for i in range(4):  # each side
            temp = 0  # get num of the side
            idx = i * (N//4)
            while idx < (i + 1) * (N//4):
                temp = temp * 16 + q[idx]
                idx += 1
            possibles.add(temp)
        q.append(q.popleft())  # rotate

    possibles = list(possibles)
    possibles.sort(reverse=True)
    print(f"#{tc} {possibles[K - 1]}")
