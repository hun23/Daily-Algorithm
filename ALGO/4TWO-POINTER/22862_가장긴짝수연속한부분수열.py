from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
for i in range(N):
    if arr[i] % 2 == 0:
        left = right = i
        break

ans = 0
delete_cnt = 0
while left <= right < N:
    # 짝수
    if arr[right] % 2 == 0:
        ans = max(ans, right - left + 1 - delete_cnt)
        right += 1
        continue
    # 홀수
    if delete_cnt < K:
        right += 1
        delete_cnt += 1
    else:
        left += 1
        while left <= right and arr[left] % 2 != 0:
            left += 1
            delete_cnt -= 1
println(ans)
