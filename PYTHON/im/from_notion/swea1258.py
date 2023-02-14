# with open("./input.txt", "r") as fr:
T = int(input())
# T = int(fr.readline().rstrip())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N = int(fr.readline().rstrip())
    # arr = [
    #     list(map(int, fr.readline().rstrip().split()))
    #     for _ in range(N)
    # ]
    answers = []
    for r in range(N):
        row_sum = sum(arr[r])
        filled = []
        if row_sum != 0:
            start = -1
            end = -1
            for c in range(N):
                if start == -1:
                    if arr[r][c] != 0:
                        start = c
                        filled.append(start)
                else:
                    if arr[r][c] == 0:
                        end = c
                        start = -1
                        filled.append(end)
                    elif c == N - 1:
                        end = c + 1
                        start = -1
                        filled.append(end)
            for i in range(0, len(filled), 2):
                start, end = filled[i], filled[i + 1]
                ridx = 0
                while arr[r + ridx][start] != 0:
                    arr[r + ridx][start:end] = [0] * (end - start)
                    ridx += 1
                    if r + ridx >= N:
                        break
                answers.append((ridx, end - start))
    answers.sort(key=lambda x: (x[0] * x[1], x[0]))
    print(f"#{tc} {len(answers)}", end=" ")
    prnt = []
    for a in answers:
        prnt.append(" ".join(map(str, a)))
    print(*prnt, sep=" ")
