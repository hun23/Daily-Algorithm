from sys import stdin, stdout

input = stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
new_arr = [0] * (N + M)
a_pointer, b_pointer = 0, 0
while not (a_pointer == N and b_pointer == M):
    if a_pointer == N:
        new_arr[a_pointer + b_pointer] = B[b_pointer]
        b_pointer += 1
    elif b_pointer == M or A[a_pointer] < B[b_pointer]:
        new_arr[a_pointer + b_pointer] = A[a_pointer]
        a_pointer += 1
    else:
        new_arr[a_pointer + b_pointer] = B[b_pointer]
        b_pointer += 1
print(*new_arr)
