def solve(A, B, C):
    if B == 1:
        return A % C
    half = solve(A, B//2, C)
    if B % 2 == 0:
        return half * half % C
    else:
        return A * half * half % C


A, B, C = map(int, input().split())
print(solve(A, B, C))
