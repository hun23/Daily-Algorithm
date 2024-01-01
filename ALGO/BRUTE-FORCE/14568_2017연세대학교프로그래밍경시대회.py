N = int(input())
ans = 0

for taek in range(1, N):
    if taek % 2 == 1:
        continue
    for young in range(1, N):
        for nam in range(young + 2, N):
            if taek + young + nam == N:
                ans += 1
print(ans)