N = int(input())
arr = list(map(int, input().split()))
mx, asc, des = 1, 1, 1
for i in range(N - 1):
    if arr[i] < arr[i + 1]:
        asc += 1
        des = 1
    elif arr[i] > arr[i + 1]:
        des += 1
        asc = 1
    else:
        asc += 1
        des += 1
    if mx < asc:
        mx = asc
    if mx < des:
        mx = des
print(mx)
