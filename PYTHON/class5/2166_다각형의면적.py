def dot_product(a, b):
    ax, ay = a
    bx, by = b
    return (ax * by - ay * bx)

N = int(input())
inputs = []
for n in range(N):
    inputs.append(tuple(map(int, input().split())))
answer = 0
for n in range(N):
    if n == N - 1:
        a, b = inputs[n], inputs[0]
    else:
        a, b = inputs[n], inputs[n + 1]
    # a, b dot product
    answer += dot_product(a, b)
    # print(answer)
print(answer/2 * (1 if answer > 0 else -1))