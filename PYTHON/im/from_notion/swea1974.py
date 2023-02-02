T = int(input())
for tc in range(1, T + 1):
    # 스도쿠 입력
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    for i in range(9):
        sets = [set(), set(), set()]  # hor, ver, box
        for j in range(9):
            h = sudoku[i][j]  # j가 증가하며 i번째 row의 가로합
            v = sudoku[j][i]  # j가 증가하며 i번째 col의 세로합
            # j가 증가하며 i번째 box의 합
            b = sudoku[(i // 3 * 3) + j // 3][(i % 3 * 3) + j % 3]
            temp = [h, v, b]
            for k in range(3):
                if temp[k] in sets[k]:  # 중복되는 숫자가 있으면
                    answer = 0  # 답은 0 이후 반복문 탈출
                    break
                else:
                    sets[k].add(temp[k])  # 중복이 없으면 각 set에 추가
            if not answer:
                break
        if not answer:
            break
    print(f"#{tc} {answer}")

# 조금 더 빠른
T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    for i in range(9):
        hsum, vsum, bsum = 0, 0, 0
        for j in range(9):
            h = sudoku[i][j]
            hsum += h
            v = sudoku[j][i]
            vsum += v
            b = sudoku[(i // 3 * 3) + j // 3][(i % 3 * 3) + j % 3]
            bsum += b
        if hsum != 45 or vsum != 45 or bsum != 45:
            answer = 0
            break
    print(f"#{tc} {answer}")
