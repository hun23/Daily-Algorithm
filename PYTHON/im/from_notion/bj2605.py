# 입력
n = int(input())
inp = list(map(int, input().split()))

# 정답
answer = []
for (i, num) in enumerate(inp):
    # 정답 배열에 (i + 1)번째 학생을
    # len(answer) - num 위치에 insert
    # num이 1 증가할수록 맨 뒤에서 한자리씩 앞으로 오기 때문
    answer.insert(len(answer) - num, str(i + 1))
print(" ".join(answer))
