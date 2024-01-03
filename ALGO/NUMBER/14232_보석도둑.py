K = int(input())
ans = []
for i in range(2, int(K**0.5) + 1):
    while K % i == 0:
        ans.append(i)
        K //= i
if K != 1:
    ans.append(K)
ans.sort()
print(len(ans))
print(*ans)