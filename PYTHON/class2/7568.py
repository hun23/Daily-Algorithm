def compare(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return "a"
    elif a[0] < b[0] and a[1] < b[1]:
        return "b"
    else:
        return 0


n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    # 키 몸무게를 튜플로 저장
    arr.append((x, y))

for i in range(len(arr)):
    big_count = 1
    for j in range(len(arr)):
        if compare(arr[i], arr[j]) == "b":
            big_count += 1
    print(big_count, end=(" " if i != len(arr) - 1 else ""))
