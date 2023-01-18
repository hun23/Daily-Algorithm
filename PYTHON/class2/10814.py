import sys

t = int(input())
# 나이 - 1이 인덱스인 리스트
ages = [list() for _ in range(200)]
for _ in range(t):
    age, name = sys.stdin.readline().rstrip().split()
    # 같은 나이는 같은 리스트에 append
    ages[int(age) - 1].append(name)
# 순회하며 출력
for (i, same_ages) in enumerate(ages):
    for name in same_ages:
        print(f"{i + 1} {name}")
