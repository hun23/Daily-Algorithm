from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")

N, K, B = map(int, input().split())
is_broken = [False] * N
for _ in range(B):
    b = int(input())
    is_broken[b - 1] = True

broken_cnt = 0
for k in range(K):
    if is_broken[k]:
        broken_cnt += 1
ans = broken_cnt
left, right = 0, K - 1
while right < N - 1:
    if is_broken[left]:
        broken_cnt -= 1
    if is_broken[right + 1]:
        broken_cnt += 1
    if ans > broken_cnt:
        ans = broken_cnt
    left += 1
    right += 1
println(ans)
