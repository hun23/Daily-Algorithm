N = int(input())
arr = list(map(int, input().split()))
new_arr = sorted(list(set(arr)))
answer = [0] * len(arr)
di = {key: value for value, key in enumerate(new_arr)}
for i in range(len(arr)):
    answer[i] = di[arr[i]]
print(*answer, sep=" ")
