A, B, C, N = map(int, input().split())

a_max, b_max, c_max = N // A, N // B, N // C
for a in range(a_max + 1):
    for b in range(b_max + 1):
        for c in range(c_max + 1):
            if A * a + B * b + C * c == N:
                print(1)
                exit()

print(0)